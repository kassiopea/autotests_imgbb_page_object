import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import importlib

from constants import Auth, Urls
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.profile_page import ProfilePage


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', help="select browser chrome or firefox", default="chrome")
    parser.addoption('--language', action='store', help="select language", default="en")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("browser")
    locate = request.config.getoption("language")
    if browser == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {'intl.accept_languages': locate})
        # browser = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     desired_capabilities=DesiredCapabilities.CHROME,
        #     browser_profile=options
        # )
        browser = webdriver.Chrome(options=options)
    elif browser == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", locate)
        # browser = webdriver.Remote(
        #     command_executor='http://localhost:4444/wd/hub',
        #     desired_capabilities=DesiredCapabilities.FIREFOX,
        #     browser_profile=fp
        # )
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()

    yield browser
    browser.quit()


@pytest.fixture(scope="class")
def setup(request, browser):
    link = Urls.LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.login_with_password(Auth.USERNAME, Auth.PASSWORD)
    page.should_be_authorized_user()
    page = ProfilePage(browser, browser.current_url)
    page.should_be_profile_url()

    def delete_all_files_in_profile_and_logout():
        profile_link = "https://{}.imgbb.com/".format(Auth.USERNAME)
        profile_page = ProfilePage(browser, profile_link)
        profile_page.open()
        profile_page.delete_all_files()
        profile_page.profile_is_empty()

        profile_page.logout()
        logout_page = LogoutPage(browser, browser.current_url)
        logout_page.should_be_logout_link()

    request.addfinalizer(delete_all_files_in_profile_and_logout)


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            module = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, module, ids=[repr(id) for id in module])


def load_from_module(module):
    return importlib.import_module("data.{}".format(module)).testdata
