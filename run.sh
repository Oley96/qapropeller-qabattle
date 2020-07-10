rm -rf allure-results

mkdir -p allure-results

rm -rf allure-report

venv/bin/pytest --remote=True --browser_ver=83.0  ./tests
