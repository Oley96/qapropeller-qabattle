rm -rf allure-results

mkdir -p allure-results

rm -rf allure-report

pytest ./tests --remote=True --browser_ver=83.0

allure serve allure-results