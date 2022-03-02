import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):

    parser.addoption('--language', action='store', default='fr', help="Choose language:")

@pytest.fixture(scope="function")
def browser(request):
    choise_language = request.config.getoption("language")
    options = Options()
    if choise_language:
        options.add_experimental_option('prefs', {'intl.accept_languages': choise_language})
        browser = webdriver.Chrome(options=options)
        print(f"Run language is {choise_language}")
    else:
        raise pytest.UsageError("--Choise language browser")

    yield browser
    print("\nquit browser...")
    browser.quit()


