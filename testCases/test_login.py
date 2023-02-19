import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readcongid
from utilities.Customlogger import LogGen

class Test_001_Login():
    baseURL = Readcongid.getApplicationURL()
    Username = Readcongid.getusername()
    Password = Readcongid.getPassword()

    logger=LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info("******* Test_001_Login********")
        self.logger.info("******* Verifing home page title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******* Verifing home page title is passed********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            assert False
            self.logger.info("******* Verifing home page title is failed********")

    def test_login(self,setup):
        self.logger.info("******* login test is started ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.Clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******* login test is passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("******* login test is failed ********")
            assert False



