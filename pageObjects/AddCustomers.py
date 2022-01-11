from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnk_Customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_Customer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_AddNew_xpath = "//a[@class='btn btn-primary']"
    txt_Email_id = "Email"
    txt_Password_id = "Password"
    txt_FirstName_css = "input#FirstName"
    txt_LastName_css = "input#LastName"
    rdbtn_GenderMale_id = "Gender_Male"
    rdbtn_GenderFemale_id = "Gender_Female"
    txt_DOB_xpath = "//input[@id='DateOfBirth']"
    txt_CompanyName_xpath = "//input[@id='Company']"
    chk_TaxExempt_xpath = "//input[@id='IsTaxExempt']"
    drp_mgrofVendor_xpath = "//select[@id='VendorId']"
    chk_Active_xpath = "//input[@id='Active']"
    txt_AdminComment_xpath = "//*[@id='AdminComment']"
    btn_Save_xpath = "//button[@name='save']"
    btn_SaveandContinue_xpath = "//button[@name='save-continue']"
    txt_Newsletter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']//input[(@class='k-input k-readonly') and (@aria-labelledby='SelectedNewsletterSubscriptionStoreIds_label')]"
    drp_Newsletter_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    txt_CustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']//input[(@class='k-input k-readonly') and (@aria-labelledby='SelectedCustomerRoleIds_label')]"
    drp_CustomerRoles_xpath = "//select[@id='SelectedCustomerRoleIds']"

    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_Customer_menu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_Customer_menuitem_xpath)

    def clickonAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_Email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.Id, self.txt_Password_id).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.CSS_SELECTOR, self.txt_FirstName_css).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.CSS_SELECTOR, self.txt_LastName_css).send_keys(lastname)

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdbtn_GenderMale_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdbtn_GenderFemale_id).click()

    def setCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.txt_CompanyName_xpath).send_keys(companyname)

    def checkTaxExempt(self):
        self.driver.find_element(By.XPATH, self.chk_TaxExempt_xpath).click()

    def checkIsActive(self):
        self.driver.find_element(By.XPATH, self.chk_Active_xpath).click()

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txt_AdminComment_xpath).send_keys(comment)

    def setmgrofVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_mgrofVendor_xpath))
        drp.select_by_index(value)

    def setNewsletter(self, value):
        drpdwn = self.driver.find_element(By.XPATH, self.drp_Newsletter_xpath)
        drp = Select(drpdwn)
        drp.select_by_value(value)

    def setCustomerRole(self, role):
        element = self.driver.find_element(By.XPATH, self.drp_CustomerRoles_xpath)
        drp = Select(element)
        drp.select_by_visible_text(role)

    def clickonSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()

    def clickonSaveContinue(self):
        self.driver.find_element(By.XPATH, self.btn_SaveandContinue_xpath).click()