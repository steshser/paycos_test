# API&UI test example
- [Prerequisites](#Prerequisites)
- [Setup](#Setup)
- [Running tests](#Running-tests)
  - [API tests](#API-tests)
  - [UI tests](#UI-tests)
- [Test results](#Test-results)
- [Continuous Integration](#Continuous-Integration)

## Prerequisites

Before running the tests, ensure you have the following prerequisites installed on your system:

- Python 3.11
- Pip
- Chrome WebDriver
- Gecko WebDriver (Firefox)
- Google Chrome browser (suitable version with Chrome WebDriver)
- Firefox browser (suitable version with Gecko WebDriver)

## Setup
1. Clone the repository to your local machine:
   https://github.com/steshser/paycos_test.git
2. Install project dependencies:
```
pip install -r requirements.txt
```

## Running tests

### API tests
To run the API tests, use the following command:
``` 
pytest api_tests/test_reqres_api.py
```
or
```
pytest -m api
```

### UI tests
To run the UI tests, use the following command:
``` 
pytest ui_tests/test_awarasleep.py
```
or
```
pytest -m ui
```

## Test results
Test results can be found in the test-reports directory. These reports are generated using Pytest and can be used to review the test outcomes.<br>
After running your tests, you can generate the Allure report using the following command:
```
allure serve ./allure-results
```

## Continuous Integration
Continuous Integration is set up using CircleCI. The configuration is defined in the .circleci/config.yml file. Tests are automatically triggered on each commit to the specified branch.