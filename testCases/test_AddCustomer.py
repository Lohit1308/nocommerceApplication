import pytest
from selenium import webdriver
from pageObjects.AddCustomers import AddCustomer
from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from testCases.test_login import Test_001_login
import time

class Test_003_AddCustomer:
    baseurl = ReadConfig.getAppUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGenerator.logGen()

    def test_add_customer(self, setUp):
        self.logger.info("************ Starting Add Customer Setup ************")
        self.logger.info("************ Test 003 Add Customer ************")
        self.driver = setUp
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.log = Test_001_login()
        self.log.test_login()



