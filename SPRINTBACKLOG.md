# Sprint Backlog - Tracquet

---

## Sprint 2 - API Connection

**Sprint Goal:** Connect a live tennis API so live match and ranking data is accessible and ready for page-level integration.

API: https://api.api-tennis.com/tennis/

**Committed Items:**

| PB ID  | User Story                                                                                |
| ------ | ----------------------------------------------------------------------------------------- |
| PB-004 | As a user, I want the app to connect to a live tennis API so that I can see current data. |

**Sprint Plan:**

| Task                             | Description                                                                | Status   |
| -------------------------------- | -------------------------------------------------------------------------- | -------- |
| Evaluate and select API provider | Compare candidate tennis APIs and confirm one provider for Sprint 2 usage. | Complete |
| Configure API credentials        | Store API key and base URL securely via environment variables.             | Complete |
| Build API service module         | Create reusable Flask service functions for API requests and parsing.      | Complete |
| Add connectivity test routes     | Add temporary/internal endpoints to verify live match/ranking payloads.    | Complete |
| Implement error handling/logging | Handle auth/network/API errors and return safe fallback responses.         | Complete |
| Validate data readiness          | Confirm required fields are available for Sprint 3 frontend integration.   | Complete |

**Unit Test Summary Table:**

| Test ID | Test Name                    | What It Tests                            | Input                                   | Expected Output                                                         | Actual Output                                                                 | Pass/Fail |
| ------- | ---------------------------- | ---------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------- | --------- |
| T2-01   | API key loaded from env      | PB-004 - secure API configuration        | Valid `.env` with API key               | App reads API key successfully and initialises API client/service       | `API_TENNIS_KEY` loaded successfully; requests authenticated with API key     | Pass      |
| T2-02   | Live matches request success | PB-004 - live data endpoint reachable    | Valid request to live matches endpoint  | HTTP 200 and structured live match data returned                        | `get_livescore` returned success payload (list structure available)           | Pass      |
| T2-03   | Rankings request success     | PB-004 - rankings endpoint reachable     | Valid request to rankings endpoint      | HTTP 200 and structured ranking data returned                           | `get_standings` returned success payload with ranking fields                  | Pass      |
| T2-04   | API auth failure handling    | PB-004 - invalid credential handling     | Invalid/expired API key                 | Graceful error response (no crash), clear error logged/message returned | API returned auth failure response; script handled failure path without crash | Pass      |
| T2-05   | Network timeout handling     | PB-004 - resilience to connection issues | Simulated timeout from provider         | Request timeout handled gracefully with fallback/error response         | Timeout scenario handled with safe failure path and no application crash      | Pass      |
| T2-06   | Required field availability  | PB-004 - data ready for Sprint 3 pages   | Sample live match and ranking responses | Required fields (names, scores/ranks, country, points, etc.) available  | Required fields confirmed present for Live, Rankings, and Player integration  | Pass      |

**Sprint Review:**  
Sprint 2 goal achieved. The API connection is operational, credentials are configured via environment variables, and live match/ranking/player data endpoints were validated. Data is now ready for Sprint 3 page integration.

**Sprint Retrospective:**  
What went well: API setup and endpoint testing were completed on schedule.  
What to improve: Expand automated tests  
Action for next sprint: Integrate API data into `live.html`, `rankings.html`, and `player.html` routes/templates with reusable service functions.
