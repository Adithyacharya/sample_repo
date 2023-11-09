# MMP Test Automation Framework

## Setup and installation

- Install Python (3.8 or newer) and virtualenv
- Create a Python virtual environment with virtualenv
  `virtualenv mmpenv`
- Activate the environment
  `. mmpenv/bin/activate`
- Install project dependencies
  `pip install -r requirements.txt`

## Executing the tests

Sample execution to run all tests:

```
pytest
```


## Test suites & test cases structure in the project

In a given execution directory, every .py file prefixed with test_ is considered as a single test suite. All the functions prefixed with test_ are considered as individual test cases.

