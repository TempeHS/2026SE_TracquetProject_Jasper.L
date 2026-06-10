# Sprint Backlog - Tracquet

---

## Sprint 1 - PWA Skeleton

**Sprint Goal:** Successfully decide on and connect an API for tennis data.  
Possible API's:

- https://tennis-api.com/

- https://rapidapi.com/jjrm365-kIFr3Nx_odV/api/tennis-api-atp-wta-itf

- https://api-tennis.com/

**Committed Items:**

| PB ID  | User Story                                                                                                 |
| ------ | ---------------------------------------------------------------------------------------------------------- |
| PB-001 | As a user, I want to securely log in so that my account is protected.                                      |
| PB-002 | As a user, I want to be brought to a dashboard after login so that I can navigate to different data pages. |
| PB-003 | As a user, I want a navbar on every page so that I can navigate the site easily.                           |

**Sprint Plan:**

| Task                                | Description                                                                              |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| Set up Flask project structure      | Initialise Flask app, configure folders for templates, static files and database.        |
| Build login page and authentication | Create login form, implement password hashing, set up user session management.           |
| Implement Google Authenticator 2FA  | Integrate Google Auth as a second factor on the login flow.                              |
| Build navbar                        | Create a consistent navbar across all pages with links to each section.                  |
| Create placeholder pages            | Build frontend templates for Dashboard, Live Matches, Rankings, and Player Search pages. |
| Connect page routing                | Set up Flask routes so all navbar links and page transitions function correctly.         |

**Unit Test Summary Table:**

| Test ID | Test Name                   | What It Tests                             | Input                                 | Expected Output                                      | Actual Output                                   | Pass/Fail |
| ------- | --------------------------- | ----------------------------------------- | ------------------------------------- | ---------------------------------------------------- | ----------------------------------------------- | --------- |
| T1-01   | Valid login                 | PB-001 - login with correct credentials   | Valid email and password              | User is redirected to Google Auth prompt             | User redirected to 2FA prompt                   | Pass      |
| T1-02   | Invalid login               | PB-001 - login with incorrect credentials | Incorrect password                    | Error message displayed, user not logged in          | Error message shown, login rejected             | Pass      |
| T1-03   | Password hashing            | PB-001 - passwords stored securely        | New user registration                 | Password is stored as a hash, not plain text         | Hash visible in database, plain text not stored | Pass      |
| T1-04   | Google Auth 2FA             | PB-001 - 2FA required on login            | Valid credentials + correct auth code | User is granted access to dashboard                  | Dashboard loaded after successful 2FA           | Pass      |
| T1-05   | Dashboard loads             | PB-002 - dashboard accessible after login | Successful login and 2FA              | Dashboard page loads with navigation options visible | Dashboard displayed correctly                   | Pass      |
| T1-06   | Navbar present on all pages | PB-003 - navbar consistent across site    | Navigate to each page                 | Navbar visible on every page                         | Navbar displayed on all pages                   | Pass      |
| T1-07   | Navbar routing              | PB-003 - navbar links function correctly  | Click each navbar link                | Correct page loads for each link                     | All pages loaded correctly                      | Pass      |

**Sprint Review:**
All Sprint 1 committed items were completed. Login with password hashing and Google Authenticator 2FA is functional. The navbar is consistent across all pages and all routes are connected. Placeholder pages are in place and ready for API data integration in Sprint 2.

**Sprint Retrospective:**
Sprint 1 went smoothly with all planned features completed within the sprint window. The login and 2FA implementation was straightforward given existing Flask experience. Going forward, the sprint backlog and unit test table will be filled in before coding begins as required by the WAgile process.
