import pytest
from selenium import webdriver
from selenium.webdriver import Ie


@pytest.fixture
def setup():
        driver = webdriver.Ie()
        return driver


# def setup(browser):
#     if browser == 'Chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome Browser.......")
#     elif browser == 'firefox':
#         driver = webdriver.firefox()
#         print("Launching Firefox Browser.......")
#     else:
#         driver = webdriver.ie()
#     return driver


# def pytest_adoption(parser):        #This will get the value from CLI
#     parser.adoption("--browser")
#
# @pytest.fixture()
# def browser(request):       #This will return the browser value in setup method
#     return request.config.getoption("--browser")
#
#
# ################pytest HTML report####################
#
# #It is hook to for Adding enviornmetn info to HTM report
#
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Avaamo'
#     config._metadata['module name'] = 'pizza'
#     config._metadata['Tester'] = 'suresh'
#
# #It is hook for delete/modify enviornment info  to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)