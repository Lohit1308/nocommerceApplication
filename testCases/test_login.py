import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator


class Test_001_login:
    baseurl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGenerator.logGen()

    def test_homepagetitle(self, setUp):
        self.logger.info("************ Test 001 Login ************")
        self.logger.info("************ Verifying Home Page Title ************")
        self.driver = setUp
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.driver.close()
            self.logger.info("************ Home Page Title Page is Passed ************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots"+"\\homepagetitle.png")
            self.driver.close()
            self.logger.error("************ Home Page Title Page is failed ************")
            assert False

    def test_login(self, setUp):
        self.logger.info("************ Verifying Login Page Title ************")
        self.driver = setUp
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************ Login Page Title Page is Passed ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots"+"\\homepagetitle.png")
            self.logger.error("************ Login Page Title Page is failed ************")
            self.driver.close()
            assert False

