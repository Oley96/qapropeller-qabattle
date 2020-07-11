# Python + Pytest + Selene + Allure + Selenoid + Jenkins demo project

## To integrate PyCharm with PyTest:
Preferences -> Tools -> Default test runner -> pytest

## How to start
- clone repo
- create virtual environment: python -m venv env && source bin/activate
- install requirements: pip install -r requirements.txt
- run selenoid, selenoid-ui, front-app: docker-compose up -d
- run tests: pytest ./tests --remote=True --browser_ver=83.0 (command line params can view in conftest.py)
- see tests executing on selenoid-ui 

## How to create allure report?
- allure-cli should be installed
- after tests finished: allure serve allure-results
- enjoy!

## How to start with jenkins?
- run jenkins
- create pipeline job (Jenkins file in the root of project)
- add git repo with tests
- download allure plugin
- add allure-cli in jenkins setting
- start job

