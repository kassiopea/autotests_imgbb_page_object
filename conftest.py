import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import importlib


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
        browser = webdriver.Chrome(options=options)
    elif browser == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", locate)
        browser = webdriver.Firefox(firefox_profile=fp)

    yield browser
    browser.quit()


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            module = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, module, ids=[repr(id) for id in module])


def load_from_module(module):
    return importlib.import_module("data.{}".format(module)).testdata
