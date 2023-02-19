import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer page
    lnkCustomers_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    inkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    texEmail_ID="Email"
    texPassword_ID ="Password"
    texFirstname_xpath="//input[@id='FirstName']"
    texLastname_xpath="//input[@id='LastName']"
    rdMaleGender_xpath="//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    texDOB_xpath="//input[@id='DateOfBirth']"
    texCompanyName_xpath="//input[@id='Company']"
    texCustomerRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath="//option[normalize-space()='Administrators']"
    lstitemForumModerator_xpath="//option[normalize-space()='Forum Moderators']"
    lstitemGuest_xpath="//option[@value='4']"
    lstitemRegistered_xpath="//option[@value='3']"
    listitemTestrole_xpath="//option[@value='6']"
    lstitemVendor_xpath="//option[@value='5']"
    droMangvendor_xpath="//select[@id='VendorId']"
    texAdmincomm_xpath="//textarea[@id='AdminComment']"
    btesave_xpath="//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickonCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def ClickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def ClickonAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.texEmail_ID).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.texPassword_ID).send_kays(password)

    def setFirstNmae(self,firstName):
        self.driver.find_element(By.XPATH,self.texFirstname_xpath).send_keys(firstName)

    def setLastNmae(self,lastName):
        self.driver.find_element(By.XPATH,self.texFirstname_xpath).send_keys(lastName)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.texCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)

        elif role == "Administrators":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)

        elif role == "Guest":
            # Hear user can be registered (or) Guest
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)

        elif role == "Vendor":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemVendor_xpath)

        elif role == "TestRole":
            self.listitem=self.driver.find_element(By.XPATH,self.listitemTestrole_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("argumenets[].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.droMangvendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH,self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.texDOB_xpath).send_keys(dob)

    def setCompanyNmae(self,copmname):
        self.driver.find_element(By.XPATH, self.texCompanyName_xpath).send_keys(copmname)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH, self.texAdmincomm_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btesave_xpath).click()














