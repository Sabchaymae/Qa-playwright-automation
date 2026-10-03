\# Test Case Document – Login Functionality



\## 1. General Information



| Field            | Details                                                           |

| ---------------- | ----------------------------------------------------------------- |

| Application      | SauceDemo                                                         |

| URL              | https://www.saucedemo.com/                                        |

| Module           | Authentication / Login                                            |

| Test Type        | Functional Testing                                                |

| Automation Tool  | Playwright + Pytest                                               |

| Browser          | Chromium                                                          |

| Test Environment | Web                                                               |

| Test Scenario    | Verify the login functionality with valid and invalid credentials |

| Total Test Cases | 6                                                                 |

| Executed Tests   | 6                                                                 |

| Passed           | 6                                                                 |

| Failed           | 0                                                                 |

| Overall Status   | PASS                                                              |



\---



\## 2. Test Scenario



\*\*TS-LOGIN-001 — Verify the Login Functionality\*\*



The objective is to verify that users can successfully log in with valid credentials and that the application correctly handles invalid or missing credentials by displaying the appropriate error messages.



\---



\# 3. Test Cases



\## TC-LOGIN-001 — Login with valid credentials



\*\*Priority:\*\* High

\*\*Test Type:\*\* Positive / Functional



\### Preconditions



\* The application is accessible.

\* The user is on the SauceDemo login page.

\* Valid credentials are available.



\### Test Data



| Field    | Value           |

| -------- | --------------- |

| Username | `standard\_user` |

| Password | `secret\_sauce`  |



\### Steps



| Step | Action                                       |

| ---- | -------------------------------------------- |

| 1    | Open the SauceDemo login page.               |

| 2    | Enter `standard\_user` in the Username field. |

| 3    | Enter `secret\_sauce` in the Password field.  |

| 4    | Click the Login button.                      |



\### Expected Result



The user is successfully authenticated and redirected to the Products page.



\### Actual Result



The user was successfully authenticated and the \*\*Products\*\* page was displayed.



\### Status



\*\*PASS\*\*



\---



\## TC-LOGIN-002 — Login with empty username



\*\*Priority:\*\* High

\*\*Test Type:\*\* Negative / Validation



\### Preconditions



\* The application is accessible.

\* The user is on the login page.



\### Test Data



| Field    | Value          |

| -------- | -------------- |

| Username | Empty          |

| Password | `secret\_sauce` |



\### Steps



| Step | Action                                      |

| ---- | ------------------------------------------- |

| 1    | Open the SauceDemo login page.              |

| 2    | Leave the Username field empty.             |

| 3    | Enter `secret\_sauce` in the Password field. |

| 4    | Click the Login button.                     |



\### Expected Result



The application displays:



`Epic sadface: Username is required`



\### Actual Result



The application displayed:



`Epic sadface: Username is required`



\### Status



\*\*PASS\*\*



\---



\## TC-LOGIN-003 — Login with empty password



\*\*Priority:\*\* High

\*\*Test Type:\*\* Negative / Validation



\### Preconditions



\* The application is accessible.

\* The user is on the login page.



\### Test Data



| Field    | Value           |

| -------- | --------------- |

| Username | `standard\_user` |

| Password | Empty           |



\### Steps



| Step | Action                                       |

| ---- | -------------------------------------------- |

| 1    | Open the SauceDemo login page.               |

| 2    | Enter `standard\_user` in the Username field. |

| 3    | Leave the Password field empty.              |

| 4    | Click the Login button.                      |



\### Expected Result



The application displays:



`Epic sadface: Password is required`



\### Actual Result



The application displayed:



`Epic sadface: Password is required`



\### Status



\*\*PASS\*\*



\---



\## TC-LOGIN-004 — Login with invalid username



\*\*Priority:\*\* High

\*\*Test Type:\*\* Negative / Functional



\### Preconditions



\* The application is accessible.

\* The user is on the login page.



\### Test Data



| Field    | Value          |

| -------- | -------------- |

| Username | `wrong\_user`   |

| Password | `secret\_sauce` |



\### Steps



| Step | Action                                      |

| ---- | ------------------------------------------- |

| 1    | Open the SauceDemo login page.              |

| 2    | Enter `wrong\_user` in the Username field.   |

| 3    | Enter `secret\_sauce` in the Password field. |

| 4    | Click the Login button.                     |



\### Expected Result



The application rejects the login attempt and displays:



`Epic sadface: Username and password do not match any user in this service`



\### Actual Result



The application rejected the login attempt and displayed the expected error message.



\### Status



\*\*PASS\*\*



\---



\## TC-LOGIN-005 — Login with invalid password



\*\*Priority:\*\* High

\*\*Test Type:\*\* Negative / Functional



\### Preconditions



\* The application is accessible.

\* The user is on the login page.



\### Test Data



| Field    | Value            |

| -------- | ---------------- |

| Username | `standard\_user`  |

| Password | `wrong\_password` |



\### Steps



| Step | Action                                        |

| ---- | --------------------------------------------- |

| 1    | Open the SauceDemo login page.                |

| 2    | Enter `standard\_user` in the Username field.  |

| 3    | Enter `wrong\_password` in the Password field. |

| 4    | Click the Login button.                       |



\### Expected Result



The application rejects the login attempt and displays:



`Epic sadface: Username and password do not match any user in this service`



\### Actual Result



The application rejected the login attempt and displayed the expected error message.



\### Status



\*\*PASS\*\*



\---



\## TC-LOGIN-006 — Login with both fields empty



\*\*Priority:\*\* High

\*\*Test Type:\*\* Negative / Validation



\### Preconditions



\* The application is accessible.

\* The user is on the login page.



\### Test Data



| Field    | Value |

| -------- | ----- |

| Username | Empty |

| Password | Empty |



\### Steps



| Step | Action                          |

| ---- | ------------------------------- |

| 1    | Open the SauceDemo login page.  |

| 2    | Leave the Username field empty. |

| 3    | Leave the Password field empty. |

| 4    | Click the Login button.         |



\### Expected Result



The application displays:



`Epic sadface: Username is required`



\### Actual Result



The application displayed:



`Epic sadface: Username is required`



\### Status



\*\*PASS\*\*



\---



\# 4. Test Execution Summary



| Metric           | Result |

| ---------------- | -----: |

| Total Test Cases |      6 |

| Passed           |      6 |

| Failed           |      0 |

| Blocked          |      0 |

| Not Executed     |      0 |

| Pass Rate        |   100% |



\## Conclusion



All six functional test cases for the SauceDemo Login functionality were successfully executed using \*\*Playwright and Pytest\*\*.



The tests cover:



\* Successful authentication

\* Required field validation

\* Invalid username

\* Invalid password

\* Empty credentials

\* Error message validation



\*\*Execution Result: PASS — 6/6 test cases passed.\*\*



