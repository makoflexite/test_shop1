import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language:English or Spanish or Russian")
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        print("\nbrowser is started on language:", user_language)
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        print("\nbrowser is started on language:", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name parameter should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()