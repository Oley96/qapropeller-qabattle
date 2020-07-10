import pytest
from selene import be
from selene.api import config
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser_ver", action="store", default="")
    parser.addoption("--remote", action="store", default=False)
    parser.addoption("--hub", action="store", default="0.0.0.0")
    parser.addoption("--headless", action="store", default=False)


def get_chrome_options(configuration):
    options = webdriver.ChromeOptions()
    options.headless = configuration["headless"]
    return options


def get_firefox_options(configuration):
    options = webdriver.FirefoxOptions()
    options.headless = configuration["headless"]
    return options


@pytest.fixture
def configuration(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browser_ver")
    hub = request.config.getoption("--hub")
    headless = False
    remote = False
    if request.config.getoption("--headless"):
        headless = True
    if request.config.getoption("--remote"):
        remote = True

    return {"remote": remote,
            "version": version,
            "browser": browser,
            "headless": headless,
            "hub": hub}


@pytest.fixture(scope='function', autouse=True)
def browser_management(configuration):
    config.base_url = 'http://192.168.4.101:8080'
    config.timeout = 10

    if configuration["remote"]:
        config.driver = create_remote_driver(configuration)
    else:
        create_local_driver(configuration)
    yield
    browser.quit()


def create_remote_driver(configuration):
    if configuration["browser"] == "chrome":
        options = get_chrome_options(configuration)
    else:
        options = get_firefox_options(configuration)

    capabilities = {
        "version": configuration["version"],
        "acceptInsecureCerts": True,
        "enableVNC": True,
        "screenResolution": "1280x1024x24"
    }

    driver = webdriver.Remote(command_executor=f"http://{configuration['hub']}:4444/wd/hub",
                              options=options,
                              desired_capabilities=capabilities)
    return driver


def create_local_driver(configuration):
    if configuration["browser"] == "chrome":
        options = get_chrome_options(configuration)
        config.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    elif configuration["browser"] == "firefox":
        options = get_firefox_options(configuration)
        config.driver = webdriver.Chrome(GeckoDriverManager().install(), options=options)


@pytest.fixture
def login():
    LoginPage().open() \
        .login_with("test", "test"). \
        avatar.should(be.visible)


@pytest.fixture
def login_by_cookie():
    LoginPage().open()
    browser.driver.add_cookie({"name": "secret", "value": "IAmSuperSeleniumMaster", "path": "/"})
    browser.driver.refresh()
