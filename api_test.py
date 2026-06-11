import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_TENNIS_KEY")
BASE_URL = "https://api.api-tennis.com/tennis/"


def test_standings():
    print("Testing ATP Standings...")
    response = requests.get(
        BASE_URL,
        params={"method": "get_standings", "event_type": "ATP", "APIkey": API_KEY},
    )
    data = response.json()
    if data.get("success") == 1:
        print("✅ Standings works!")
        print(
            f"   Top player: {data['result'][0]['player']} - {data['result'][0]['points']} pts"
        )
    else:
        print("❌ Standings failed:", data)


def test_livescore():
    print("Testing Livescore...")
    response = requests.get(
        BASE_URL, params={"method": "get_livescore", "APIkey": API_KEY}
    )
    data = response.json()
    if data.get("success") == 1:
        matches = data["result"]
        print(f"✅ Livescore works! {len(matches)} live matches found")
    else:
        print("❌ Livescore failed:", data)


def get_player_data(player_key):
    """Fetch detailed data for a single player by their player_key."""
    response = requests.get(
        BASE_URL,
        params={
            "method": "get_players",
            "player_key": player_key,
            "APIkey": API_KEY,
        },
    )
    data = response.json()
    if data.get("success") == 1 and data.get("result"):
        return data["result"][0]
    return None


def get_standings_data(event_type="ATP"):
    """Fetch the full standings list (used to look up points by player_key)."""
    response = requests.get(
        BASE_URL,
        params={
            "method": "get_standings",
            "event_type": event_type,
            "APIkey": API_KEY,
        },
    )
    data = response.json()
    if data.get("success") == 1:
        return data["result"]
    return []


def print_player_profile(player):
    """Print a formatted profile from player data."""
    rank, points = get_current_ranking(player)
    print("=" * 40)
    print(f"Name:        {player.get('player_name', 'N/A')}")
    print(f"Country:     {player.get('player_country', 'N/A')}")
    print(f"Birthday:    {player.get('player_bday', 'N/A')}")
    print(f"Rank:        {rank}")
    print(f"Points:      {points}")
    print(f"Cover Photo: {player.get('player_logo', 'N/A')}")
    print("=" * 40)


def get_current_ranking(player):
    """Get rank from stats and points from standings."""
    rank = player.get("player_atp_ranking") or "N/A"
    points = "N/A"

    # Rank: fall back to latest singles stats entry
    if rank == "N/A":
        singles = [s for s in player.get("stats", []) if s.get("type") == "singles"]
        if singles:
            latest = max(singles, key=lambda s: s.get("season", "0"))
            rank = latest.get("rank") or "N/A"

    # Points: look up the player in the standings by player_key
    player_key = str(player.get("player_key", ""))
    for entry in get_standings_data("ATP"):
        if str(entry.get("player_key", "")) == player_key:
            points = entry.get("points", "N/A")
            if rank == "N/A":
                rank = entry.get("place", "N/A")
            break

    return rank, points


def _to_int(value):
    """Safely convert a stat value to int (empty strings -> 0)."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def get_player_stats(player):
    """Print aggregated career totals (won/lost/played/titles)."""
    stats = player.get("stats", [])
    if not stats:
        print("   No statistics available.")
        return

    totals = {}  # type -> {won, lost, titles}
    for season in stats:
        s_type = season.get("type", "unknown")
        bucket = totals.setdefault(s_type, {"won": 0, "lost": 0, "titles": 0})
        bucket["won"] += _to_int(season.get("matches_won"))
        bucket["lost"] += _to_int(season.get("matches_lost"))
        bucket["titles"] += _to_int(season.get("titles"))

    grand = {"won": 0, "lost": 0, "titles": 0}
    for s_type, b in totals.items():
        played = b["won"] + b["lost"]
        print(
            f"   {s_type.title():14} "
            f"Played: {played:<4} Won: {b['won']:<4} "
            f"Lost: {b['lost']:<4} Titles: {b['titles']}"
        )
        for k in grand:
            grand[k] += b[k]

    grand_played = grand["won"] + grand["lost"]
    print(
        f"   {'CAREER TOTAL':14} "
        f"Played: {grand_played:<4} Won: {grand['won']:<4} "
        f"Lost: {grand['lost']:<4} Titles: {grand['titles']}"
    )


def get_player_history(player_key, days_back=365):
    """Fetch and print recent match history via the fixtures endpoint."""
    date_stop = datetime.now()
    date_start = date_stop - timedelta(days=days_back)
    response = requests.get(
        BASE_URL,
        params={
            "method": "get_fixtures",
            "player_key": player_key,
            "date_start": date_start.strftime("%Y-%m-%d"),
            "date_stop": date_stop.strftime("%Y-%m-%d"),
            "APIkey": API_KEY,
        },
    )
    data = response.json()
    matches = data.get("result", []) if data.get("success") == 1 else []

    if not matches:
        print("   No match history available.")
        return

    for match in matches[:15]:  # limit output
        print(
            f"   {match.get('event_date', 'N/A')}: "
            f"{match.get('event_first_player', 'N/A')} vs "
            f"{match.get('event_second_player', 'N/A')} "
            f"({match.get('event_final_result', 'N/A')}) "
            f"- {match.get('tournament_name', 'N/A')}"
        )


def test_player(player_key):
    """Run a full test on an individual player's data."""
    print(f"Testing Player Data (key={player_key})...")
    player = get_player_data(player_key)
    if player is None:
        print("❌ Player data failed or not found.")
        return
    print("✅ Player data works!")
    print_player_profile(player)
    print("\n📊 Statistics:")
    get_player_stats(player)
    print("\n📅 Match History:")
    get_player_history(player)


if __name__ == "__main__":
    test_standings()
    test_livescore()
    # Example player_key — replace with a real one (e.g. Novak Djokovic)
    test_player(player_key=1905)
