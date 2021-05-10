# MindTickle - REST API Test Automation Framework (Assignment)

#### PyTest based framework for automating REST API Testing
---

### Main Features:
1. REST API automation
2. Parallel Execution of test cases
3. Data factories for random test data generation using dataclasses library
4. Wrapper on python's requests module for executing REST Apis
5. Response validation using dataclasses
6. Test configuration as .ini files
7. SQL Server Database connector (Not needed in current test cases. Added as capability)
8. Generate reports in the form of HTML, XML using PyTest
9. Utilities to support runtime data
10. Project dependencies are mentioned in the dependencies.txt for quick installation of libraries
---

## Prerequisites 
* Python 3.7 or above

---

## How to use this framework
- [ ] Check out the project
- [ ] Create venv in project 
    - $ python -m venv <project_path>
- [ ] Activate virtual environment
    - $ venv\Scripts\activate
- [ ] Install all project dependencies
    - $ pip install -r dependencies.txt

---

## Run Tests
-  Run all test cases 
    - $ pytest
-  Run test cases using marker (user, pet are custom markers)
    - $ pytest -m user
    - $ pytest -m pet
- Run test cases under directory
    - $ pytest <absolute_path_to_directory>
- Run test cases from file
    - $ pytest file.py 
- Run test cases parallely 
    - $ pytest -n <worker_count> 

---

## Tech Stack

The framework is python3 based and uses the following libraries and plugins to support different functionalities.

Library/Plugin | Version 
------------ | ------------- 
dataclasses  | 0.6 |  Supported from Python3.7
dataclasses-jsonschema | 2.14.1
dict-to-dataclass | 0.0.8
Faker | 8.1.2 | Generating random data
pymssql | 2.2.1 | Communicate with SQL Serve database
pytest | 6.2.4
pytest-forked | 1.3.0
pytest-html | 3.1.1
pytest-logger | 0.5.1
pytest-metadata | 1.11.0
pytest-xdist | 2.2.1
python-dateutil | 2.8.1
requests | 2.25.1
---

## Future Scope / Enhancements:
- Integration with TestRail/ JIRA 
- Integration with Jenkins for CI/CD
- Logging results in Database
- Support for databases like sqlite, mysql, mongodb, etc.
- Data encoder and decoders for json and xml
- Test data parameterisation (Supported by PyTest)

