\# QA Automation Framework



A professional QA automation framework built with \*\*Python, Playwright, Pytest and Requests\*\*, covering UI functional testing, API testing, test reporting and Continuous Integration.



\## 🧪 Project Overview



This project demonstrates an end-to-end approach to software testing through automated tests for:



\* 🔐 Login functionality

\* 🛒 Shopping cart operations

\* 💳 Checkout process

\* 🌐 REST API testing

\* 📸 Automatic screenshots on test failures

\* 📊 HTML test reporting

\* ⚙️ Continuous Integration with GitHub Actions



\## 🛠️ Tech Stack



\* \*\*Language:\*\* Python 3.11

\* \*\*UI Automation:\*\* Playwright

\* \*\*Test Framework:\*\* Pytest

\* \*\*API Testing:\*\* Requests

\* \*\*Reporting:\*\* pytest-html

\* \*\*Design Pattern:\*\* Page Object Model (POM)

\* \*\*CI/CD:\*\* GitHub Actions

\* \*\*Version Control:\*\* Git



\## 📊 Test Coverage



| Module        |  Tests |

| ------------- | -----: |

| Login         |      6 |

| Shopping Cart |      7 |

| Checkout      |      6 |

| REST API      |      4 |

| \*\*Total\*\*     | \*\*23\*\* |



The test suite covers both \*\*positive and negative scenarios\*\*, including validation errors, invalid credentials, missing checkout information and API error responses.



\## 📁 Project Structure



```text

qa-playwright-automation/

│

├── .github/

│   └── workflows/

│       └── tests.yml

│

├── pages/

│   ├── login\_page.py

│   ├── products\_page.py

│   ├── cart\_page.py

│   └── checkout\_page.py

│

├── tests/

│   ├── test\_login.py

│   ├── test\_cart.py

│   ├── test\_checkout.py

│   └── test\_api.py

│

├── test-cases/

├── screenshots/

├── conftest.py

├── pytest.ini

├── requirements.txt

├── .gitignore

└── README.md

```



\## 🚀 Installation



Clone the repository and navigate to the project directory.



Create a virtual environment:



```bash

python -m venv .venv

```



Activate it on Windows:



```cmd

.venv\\Scripts\\activate

```



Install the dependencies:



```bash

pip install -r requirements.txt

```



Install Playwright browsers:



```bash

playwright install

```



\## ▶️ Run Tests



Run the complete test suite:



```bash

pytest -v

```



Generate an HTML report:



```bash

pytest --html=reports/report.html --self-contained-html

```



The report is generated in:



```text

reports/report.html

```



\## 📸 Failure Screenshots



The framework automatically captures a screenshot whenever a UI test fails.



Screenshots are stored in:



```text

screenshots/

```



This makes it easier to investigate and reproduce test failures.



\## 🧩 Page Object Model



The UI automation framework follows the \*\*Page Object Model (POM)\*\* design pattern.



Each application page has its own class containing:



\* Page locators

\* User actions

\* Page-specific elements



This improves test readability, maintainability and reusability.



\## 🌐 API Testing



REST API tests are implemented using the `Requests` library.



The API test suite validates:



\* HTTP status codes

\* JSON response structure

\* Response data

\* Successful resource creation

\* Non-existent resource handling



The project uses \*\*JSONPlaceholder\*\* as a public demo API for API testing.



\## ⚙️ Continuous Integration



GitHub Actions automatically executes the test suite on:



\* Pushes to `main`

\* Pull requests targeting `main`



The CI pipeline:



1\. Checks out the repository

2\. Installs Python

3\. Installs project dependencies

4\. Installs Playwright

5\. Executes the automated tests



\## 📋 QA Practices Demonstrated



This project demonstrates practical QA skills including:



\* Functional testing

\* Positive and negative testing

\* Test case design

\* UI automation

\* REST API testing

\* Assertions and validations

\* Page Object Model

\* Bug investigation

\* Failure screenshots

\* Test reporting

\* Continuous Integration

\* Git and GitHub workflow



\## 🎯 Purpose



This project was developed as a \*\*QA Automation portfolio project\*\* to demonstrate practical skills in software testing, test automation and CI/CD.



\## 👩‍💻 Author



\*\*Chaymae Kharrab\*\*



State Engineer in Computer Engineering

QA / Software Testing \& Automation



