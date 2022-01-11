import pytest
from pytest_metadata.plugin import metadata
from selenium import webdriver


@pytest.fixture()
def setUp(browser):
    if browser == 'ie':
        driver = webdriver.Ie()
        print(" Launching Internet Explorer Browser ---------- ")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print(" Launching Firefox Browser ---------- ")
    else:
        driver = webdriver.Chrome()
        print(" Launching Chrome Browser ---------- ")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####### Pytest HTML report

# to add enviroment the data into reports
"""def pytest_configure(config):
    config._metada['Project Name'] = 'nop commerce'
    config._metada['Module'] = 'Customers'

@pytest.mark.optionalhook
def pytest._metadata(metadata):
    metadata.pop("Java Home", None)
"""