import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
from utilities import XLUtils
import time


class Test_002_login_DDT:
    baseurl = ReadConfig.getAppUrl()
    logger = LogGenerator.logGen()
    path = ".\\TestData\\Login.xlsx"

    def test_login(self, setUp):
        self.logger.info("************ Starting Test 002 Login DDT ************")
        self.logger.info("************ Verifying Login Page Title ************")
        self.driver = setUp
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.row = XLUtils.getRowCount(self.path, 'Sheet1')
        lst = []   # Empty list variable

        for r in range(2, self.row+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** Passed ****")
                    self.lp.clickLogout()
                    lst.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** Failed ****")
                    self.lp.clickLogout()
                    lst.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** Failed ****")
                    lst.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** Passed ****")
                    lst.append("Pass")

        if "Fail" not in lst:
            self.logger.info("********* Login DDt Test Case is passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DDT Test Case is failed *******")
            self.driver.close()
            assert False

        self.logger.info("********* Completed Test 02 DDT Login ***************")

