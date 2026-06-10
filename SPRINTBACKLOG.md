# Sprint Backlog - Tracquet

---

## Sprint 2 - API Connection

**Sprint Goal:** Connect a live tennis API so live match and ranking data is accessible and ready for page-level integration.

Possible API's:

- https://tennis-api.com/

- https://rapidapi.com/jjrm365-kIFr3Nx_odV/api/tennis-api-atp-wta-itf

- https://api-tennis.com/

**Committed Items:**

| PB ID  | User Story                                                                                |
| ------ | ----------------------------------------------------------------------------------------- |
| PB-004 | As a user, I want the app to connect to a live tennis API so that I can see current data. |

**Sprint Plan:**

| Task                             | Description                                                                |
| -------------------------------- | -------------------------------------------------------------------------- |
| Evaluate and select API provider | Compare candidate tennis APIs and confirm one provider for Sprint 2 usage. |
| Configure API credentials        | Store API key and base URL securely via environment variables.             |
| Build API service module         | Create reusable Flask service functions for API requests and parsing.      |
| Add connectivity test routes     | Add temporary/internal endpoints to verify live match/ranking payloads.    |
| Implement error handling/logging | Handle auth/network/API errors and return safe fallback responses.         |
| Validate data readiness          | Confirm required fields are available for Sprint 3 frontend integration.   |

**Unit Test Summary Table:**

| Test ID | Test Name                    | What It Tests                            | Input                                   | Expected Output                                                         | Actual Output | Pass/Fail |
| ------- | ---------------------------- | ---------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ------------- | --------- |
| T2-01   | API key loaded from env      | PB-004 - secure API configuration        | Valid `.env` with API key               | App reads API key successfully and initialises API client/service       | Pending       | Pending   |
| T2-02   | Live matches request success | PB-004 - live data endpoint reachable    | Valid request to live matches endpoint  | HTTP 200 and structured live match data returned                        | Pending       | Pending   |
| T2-03   | Rankings request success     | PB-004 - rankings endpoint reachable     | Valid request to rankings endpoint      | HTTP 200 and structured ranking data returned                           | Pending       | Pending   |
| T2-04   | API auth failure handling    | PB-004 - invalid credential handling     | Invalid/expired API key                 | Graceful error response (no crash), clear error logged/message returned | Pending       | Pending   |
| T2-05   | Network timeout handling     | PB-004 - resilience to connection issues | Simulated timeout from provider         | Request timeout handled gracefully with fallback/error response         | Pending       | Pending   |
| T2-06   | Required field availability  | PB-004 - data ready for Sprint 3 pages   | Sample live match and ranking responses | Required fields (names, scores/ranks, country, points, etc.) available  | Pending       | Pending   |

**Sprint Review:**  
To be completed at the end of Sprint 2.

**Sprint Retrospective:**  
To be completed at the end of Sprint 2.
