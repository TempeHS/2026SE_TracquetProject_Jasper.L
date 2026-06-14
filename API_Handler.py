import requests
import os
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_TENNIS_KEY")
BASE_URL = "https://api.api-tennis.com/tennis/"

api_log = logging.getLogger(__name__)


def _request(params):
    """Shared request helper with error handling. Returns result list or None."""
    params["APIkey"] = API_KEY
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
        if data.get("success") == 1:
            return data.get("result", [])
        api_log.warning(f"API call unsuccessful: {params.get('method')}")
        return None
    except requests.exceptions.RequestException as e:
        api_log.error(f"API request failed: {e}")
        return None


def _to_int(value):
    """Safely convert a stat value to int (empty strings -> 0)."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def get_live_matches():
    """For live.html - returns list of live match dicts (or None on error)."""
    result = _request({"method": "get_livescore"})
    if result is None:
        return None

    matches = []
    for m in result:
        scores = m.get("scores", [])
        # Build per-set score list, sorted by set number
        sets = sorted(scores, key=lambda s: _to_int(s.get("score_set")))
        set_scores = [
            {
                "set": s.get("score_set", ""),
                "first": s.get("score_first", "-"),
                "second": s.get("score_second", "-"),
            }
            for s in sets
        ]

        # Current game points (e.g. "30 - 40"), and who is serving
        game_result = m.get("event_game_result", "")
        serve = m.get("event_serve")  # "First Player" / "Second Player" / None

        matches.append(
            {
                "player1": m.get("event_first_player", "N/A"),
                "player2": m.get("event_second_player", "N/A"),
                "logo1": m.get("event_first_player_logo") or "",
                "logo2": m.get("event_second_player_logo") or "",
                "set_scores": set_scores,
                "game_points": game_result,
                "serve1": serve == "First Player",
                "serve2": serve == "Second Player",
                "tournament": m.get("tournament_name", "N/A"),
                "status": m.get("event_status", ""),
            }
        )

    # Sort alphabetically by tournament so matches group together
    matches.sort(key=lambda match: match["tournament"].lower())
    return matches


def get_rankings(event_type="ATP"):
    """For rankings.html - returns list of ranked player dicts (or None on error)."""
    result = _request({"method": "get_standings", "event_type": event_type})
    if result is None:
        return None

    rankings = []
    for entry in result:
        rankings.append(
            {
                "rank": entry.get("place", "N/A"),
                "name": entry.get("player", "N/A"),
                "country": entry.get("country", "N/A"),
                "points": entry.get("points", "N/A"),
                "movement": entry.get("movement", "same"),
                "id": entry.get("player_key", ""),
            }
        )
    return rankings


def get_dashboard_preview(event_type="ATP", match_limit=3, rank_limit=5):
    """Returns a small subset of live matches and rankings for the dashboard."""
    matches = get_live_matches() or []
    rankings = get_rankings(event_type) or []
    return {
        "matches": matches[:match_limit],
        "rankings": rankings[:rank_limit],
    }


def get_player(player_key):
    """For player.html - returns single player dict (or None if not found)."""
    result = _request({"method": "get_players", "player_key": player_key})
    if not result:
        return None

    player = result[0]

    # Aggregate career stats
    stats = player.get("stats", [])
    won = lost = titles = 0
    for season in stats:
        won += _to_int(season.get("matches_won"))
        lost += _to_int(season.get("matches_lost"))
        titles += _to_int(season.get("titles"))
    played = won + lost
    win_rate = f"{round((won / played) * 100)}%" if played else "N/A"

    # Look up rank/points from standings - check BOTH ATP and WTA
    rank = "N/A"
    points = "N/A"
    for event_type in ("ATP", "WTA"):
        standings = _request(
            {"method": "get_standings", "event_type": event_type}
        ) or []
        for entry in standings:
            if str(entry.get("player_key", "")) == str(player_key):
                rank = entry.get("place", "N/A")
                points = entry.get("points", "N/A")
                break
        if rank != "N/A":  # Found them, stop searching
            break

    return {
        "id": player_key,
        "name": player.get("player_name", "N/A"),
        "country": player.get("player_country", "N/A"),
        "bday": player.get("player_bday", "N/A"),
        "logo": player.get("player_logo", ""),
        "rank": rank,
        "points": points,
        "wins": won,
        "losses": lost,
        "titles": titles,
        "win_rate": win_rate,
    }


def search_players(query):
    """Search ranked players by name across ATP and WTA standings.

    Returns a list of matching player dicts (may be empty).
    """
    query = query.strip().lower()
    if not query:
        return []

    results = []
    for event_type in ("ATP", "WTA"):
        standings = (
            _request({"method": "get_standings", "event_type": event_type}) or []
        )
        for entry in standings:
            name = entry.get("player", "")
            if query in name.lower():
                results.append(
                    {
                        "id": entry.get("player_key", ""),
                        "name": name,
                        "country": entry.get("country", "N/A"),
                        "rank": entry.get("place", "N/A"),
                        "points": entry.get("points", "N/A"),
                        "tour": event_type,
                    }
                )
    return results
