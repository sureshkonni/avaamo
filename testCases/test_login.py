import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Welcome:
    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info("*****************Test_001_Login*****************")
        self.logger.info("*****************Verifying HomePage Title*****************")
        self.driver=setup
        self.logger.info("****Opening URL****")
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.implicitly_wait(5)

        if act_title == 'This is how the chat agent shows up':

            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.implicitly_wait(5)
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

