import requests
import os
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


if __name__ == "__main__":
    test_standings()
    test_livescore()
