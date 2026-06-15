# Sprint Backlog - Tracquet

---

## Sprint 3 - API Integration

**Sprint Goal:** Integrate live API data into the Live Matches, Rankings, and Player Profile pages, finalise all pages, and add supporting features (dashboard previews, player search, caching).

**Committed Items:**

| PB ID  | User Story                                                                                          |
| ------ | --------------------------------------------------------------------------------------------------- |
| PB-005 | As a user, I want to view live match scores so that I can follow matches in real time.              |
| PB-006 | As a user, I want to view player rankings so that I can see who the top players are.                |
| PB-007 | As a user, I want to click a player name to view their profile so that I can learn more about them. |
| PB-008 | As a user, I want data on the pages organised so that I can view it logically.                      |

**Sprint Plan:**

| Task                                | Description                                                                       | Status   |
| ----------------------------------- | --------------------------------------------------------------------------------- | -------- |
| Integrate live matches page         | Render live scores with per-set scores, current game points, and serve indicator. | Complete |
| Integrate rankings page (ATP + WTA) | Display side-by-side men's and women's rankings with movement indicators.         | Complete |
| Integrate player profile page       | Render player profile with photo, country, rank, points, and career stats.        | Complete |
| Build dashboard previews            | Show live match and ATP/WTA ranking previews on the dashboard.                    | Complete |
| Implement player search             | Add navbar search returning matching players linking to profiles.                 | Complete |
| Resolve CSP for external images     | Allow player logo images from the API host within Content Security Policy.        | Complete |
| Add response caching                | Cache standings/livescore responses to improve load time and resilience.          | Complete |

**Unit Test Summary Table:**

| Test ID | Test Name                      | What It Tests                         | Input                                     | Expected Output                                                       | Actual Output                                                       | Pass/Fail |
| ------- | ------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- | --------- |
| T3-01   | Live matches render            | PB-005 - live scores display          | Live API response with active matches     | Live page shows players, per-set scores, game points grouped by event | Live matches displayed grouped by tournament with set/point detail  | Pass      |
| T3-02   | Rankings render (ATP + WTA)    | PB-006 - rankings display             | ATP and WTA standings responses           | Two ranking tables show rank, name, country, points                   | Side-by-side ATP/WTA tables rendered with movement indicators       | Pass      |
| T3-03   | Player profile loads           | PB-007 - profile from ranking link    | Valid `player_key` via `/player.html?id=` | Profile shows name, photo, country, rank, points, career stats        | Player profile rendered correctly for both ATP and WTA players      | Pass      |
| T3-04   | WTA player rank/points resolve | PB-007 - cross-tour standings lookup  | WTA player not present in ATP standings   | Rank and points resolved from WTA standings (not N/A)                 | WTA rank/points correctly resolved after searching both tours       | Pass      |
| T3-05   | Live matches sorted            | PB-008 - logical data organisation    | Multiple live matches across tournaments  | Matches grouped/ordered by tournament name                            | Matches sorted and grouped by tournament                            | Pass      |
| T3-06   | Player search returns matches  | PB-007 - search to profile navigation | Partial player name query                 | Matching players listed with link to profile                          | Search returned matching ATP/WTA players linking to profiles        | Pass      |
| T3-07   | API failure fallback           | PB-006 - resilience via cache         | Simulated standings API failure           | Stale cached rankings served instead of empty/error                   | Cached rankings served on API failure; preview no longer disappears | Pass      |

**Sprint Review:**  
Sprint 3 goal achieved. Live match, rankings (ATP + WTA), and player profile pages are integrated with live API data and finalised. Dashboard previews, player search, external-image CSP handling, and response caching were added. Caching also resolved intermittent missing-ranking and slow-load issues.

**Sprint Retrospective:**  
What went well: All committed pages integrated on schedule; caching improved performance and resilience.  
What to improve: Earlier handling of cross-tour (WTA) data lookups and CSP for external resources would have saved debugging time.  
Action for next sprint: Conduct UAT and client feedback, complete PWA testing (offline/install), and debug any issues found.
