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


def get_live_matches():
    """For live.html - returns list of live match dicts (or None on error)."""
    # TODO: call _request({"method": "get_livescore"})
    # TODO: parse into template-friendly dicts:
    #       {player1, player2, score1, score2, tournament, set}
    return []


def get_rankings(event_type="ATP"):
    """For rankings.html - returns list of ranked player dicts (or None on error)."""
    # TODO: call _request({"method": "get_standings", "event_type": event_type})
    # TODO: parse into:
    #       {rank, name, country, points, id}
    #       (wins/losses not in standings - omit or fetch separately)
    return []


def get_player(player_key):
    """For player.html - returns single player dict (or None if not found)."""
    # TODO: call _request({"method": "get_players", "player_key": player_key})
    # TODO: combine with stats aggregation (reuse your api_test logic)
    return None
