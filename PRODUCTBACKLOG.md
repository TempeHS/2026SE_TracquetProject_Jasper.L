# Product Backlog - Tracquet

## Vision

A Flask PWA that gives tennis fans a single place to view live match scores, player rankings, and individual player data for both men's and women's tennis, with secure user authentication.

## Backlog

| ID     | User Story                                                                                                 | Priority | Acceptance Criteria                                                                                                                   | Status   |
| ------ | ---------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| PB-001 | As a user, I want to securely log in so that my account is protected.                                      | High     | Login form accepts email and password. Passwords are hashed. Google Auth 2FA is required on login. Invalid credentials show an error. | Complete |
| PB-002 | As a user, I want to be brought to a dashboard after login so that I can navigate to different data pages. | High     | Dashboard displays after successful login. Links/previews to Live Matches and Rankings pages are visible.                             | Complete |
| PB-003 | As a user, I want a navbar on every page so that I can navigate the site easily.                           | Medium   | Navbar is present on all pages. All page links function correctly.                                                                    | Complete |
| PB-004 | As a user, I want the app to connect to a live tennis API so that I can see current data.                  | High     | API is connected. Live match and ranking data is accessible and ready for display.                                                    | Complete |
| PB-005 | As a user, I want to view live match scores so that I can follow matches in real time.                     | High     | Live Matches page displays current match data including players, score, location and time elapsed.                                    | Complete |
| PB-006 | As a user, I want to view player rankings so that I can see who the top players are.                       | High     | Rankings page displays a table of players with rank, name, country, age and points.                                                   | Complete |
| PB-007 | As a user, I want to click a player name to view their profile so that I can learn more about them.        | High     | Clicking a player name on the Rankings page loads their individual player page with name, image, rank, age, country and description.  | Complete |
| PB-008 | As a user, I want data on the pages organised so that I can view it logically.                             | Medium   | Live matches are grouped/sorted by tournament; rankings display movement indicators.                                                  | Complete |
| PB-009 | As a user, I want to favourite pages so that I can quickly access the ones I use most.                     | Low      | Users can favourite pages. Favourited pages are accessible from the dashboard.                                                        | To Do    |

## Changelog

| Date       | Change                                                                                    | Reason                                            |
| ---------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 2026-06-04 | Added PB-001 to PB-009 from Phase 1 requirements and Phase 2 specifications.              | Initial backlog setup for Sprint 1.               |
| 2026-06-10 | Updated statuses for Sprint 2 kickoff (PB-004 moved to In Progress; Sprint docs aligned). | Begin Sprint 2 focus on API connection milestone. |
| 2026-06-14 | Marked PB-005, PB-006, PB-007, PB-008 Complete after Sprint 3 page integration.           | Sprint 3 API integration milestone delivered.     |
