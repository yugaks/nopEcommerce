import random
import string
import time
from datetime import time
from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import Readcongid
from utilities.Customlogger import LogGen


class Test_003_AddCustomer:
    baseURL = Readcongid.getApplicationURL()
    Username = Readcongid.getusername()
    Password = Readcongid.getPassword()
    logger=LogGen.loggen()

    def test_AddCustomer(self,setup):
        self.logger.info("******* Test_003_AddCustomer ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.Clicklogin()
        self.logger.info("******* Successfull login ********")

        self.logger.info("******* Start Adding customer ********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickonCustomerMenu()
        self.driver.implicitly_wait(20)

        self.addcust.ClickOnCustomerMenuItem()
        self.addcust.ClickonAddnew()

        self.logger.info("**** Providing customer info")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstNmae("Ravi")
        self.addcust.setLastNmae("yuga")
        self.addcust.setGender("Male")
        self.addcust.setDOB("20/08/1993")
        self.addcust.setCompanyNmae("infosys")
        self.addcust.setCustomerRole("Guest")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("**saving customer info***")

        self.logger.info("** Add customer validation started ***")

        self.meg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.meg)
        if 'The new customer has been added successfully.' in self.meg:
            assert True == True
            self.logger.info("** Add customer test passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcust_scr.png")
            self.logger.info("** Add customer test failed ***")
            assert False == False

        self.driver.close()
        self.logger.info("** Editing home page title ***")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))









