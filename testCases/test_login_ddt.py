import time
from idlelib.multicall import r

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readcongid
from utilities.Customlogger import LogGen
from utilities import XLUtilities

class Test_002_DDT_Login():
    baseURL = Readcongid.getApplicationURL()
    path=".//TestData/Logindataexl.xlsx"
    logger=LogGen.loggen()


    def test_login_ddt(self,setup):
        self.logger.info("******* Test_002_DDT_Login ********")
        self.logger.info("******* login test is started ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        XLUtilities.getRowCount(self.path,'Sheet1')

        st_status=[]

        for i in range(2,self.Row+1):
            self.user=XLUtilities.readData(self.path,'sheet1',r,1)
            self.password = XLUtilities.readData(self.path,'sheet1',r,2)
            self.exp=XLUtilities.readData(self.path, 'sheet1', r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("***passed**")
                    self.lp.clickLogout();
                    st_status.append("pass")
                elif self.exp=='Fail':
                    self.logger.info("***Failed**")
                    self.lp.clickLogout();
                    st_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("***passed**")
                    self.lp.clickLogout();
                elif self.exp=='Fail':
                    self.logger.info("***passed**")
                    st_status.append("pass")

        if 'Fail' not in st_status:
            self.logger.info("****Login DDT passed***")
            self.driver.close()
            assert True
        else:
            self.logger.info("****Login DDT failed***")
            self.driver.close()
            assert False













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

