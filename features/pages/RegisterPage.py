from selenium.webdriver.common.by import By
from .BasePage import BasePage
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    password_confirm_id = "input-confirm"
    agree_name = "agree"
    continue_xpath = "//input[@value='Continue']"
    #validation
    first_name_error_xpath = "//div[contains(text(), 'First Name')]"
    last_name_error_xpath = "//div[contains(text(), 'Last Name')]"
    email_error_xpath = "//div[contains(text(), 'E-Mail Address')]"
    telephone_error_xpath = "//div[contains(text(), 'Telephone')]"
    password_error_xpath = "//div[contains(text(), 'Password')]"


    def register_first_name(self, first_name):
        self.send_text_to_element("first_name_id", self.first_name_id, first_name)


    def register_last_name(self, last_name):
        self.send_text_to_element("last_name_id", self.last_name_id, last_name)


    def register_email_id(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        email = "johnmathew" + time_stamp + "@gmail.com"

        self.send_text_to_element("email_id", self.email_id, email)
        return email

    def register_email(self, email_id):
        self.send_text_to_element("email_id", self.email_id, email_id)

    # def register_email(self, email_id=None):
    #     if email_id is None:
    #         time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    #         email_id = "johnmathew" + time_stamp + "@gmail.com"
    #     self.send_text_to_element("email_id", self.email_id, email_id)
    #     return email_id

    def register_telephone(self, telephone):
        self.send_text_to_element("telephone_id", self.telephone_id, telephone)

    def register_password(self, password):
        self.send_text_to_element("password_id", self.password_id, password)

    def register_password_confirm(self, password):
        self.send_text_to_element("password_confirm_id", self.password_confirm_id, password)

    def register_agree(self):
        self.click_on_element("agree_name", self.agree_name)

    def register_continue(self):
        self.click_on_element("continue_xpath", self.continue_xpath)

    def account_created(self):
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(expected_text)

    def existing_email(self):
        email_text = "mk.korate@gmail.com"
        self.driver.find_element(By.ID, self.email_id).send_keys(email_text)


    def email_already_registered(self):
        expected_message = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//*[contains(text(), 'Warning')]").text.__contains__(expected_message)

    def first_name_warning(self, error_message):
        # first_name_message=self.driver.find_element(By.XPATH,"").text
        # return first_name_message
        self.validation_error("first_name_error_xpath", self.first_name_error_xpath, error_message)

    def last_name_warning(self, error_message):
        self.validation_error("last_name_error_xpath", self.last_name_error_xpath, error_message)


    def email_warning(self, error_message):
        # email_warning_message = self.driver.find_element(By.XPATH,"").text
        # return email_warning_message
        self.validation_error("email_error_xpath", self.email_error_xpath, error_message)

    def telephone_warning(self, error_message):
       self.validation_error("telephone_error_xpath", self.telephone_error_xpath, error_message)

    def password_warning(self, error_message):
        self.validation_error("password_error_xpath", self.password_error_xpath, error_message)

    def email_without_at(self):
        email_input = self.driver.find_element(By.ID, self.email_id)
        email_input.clear()
        email_input.send_keys("margmail")
        return email_input
    def email_alert(self):
        email_input = self.email_without_at()
        expected_text = "Please include an '@' in the email address."
        try:
            wait = WebDriverWait(self.driver, 10)
            alert = wait.until(expected_conditions.alert_is_present())
            # alert = self.driver.switch_to.alert
            alert_text = alert.text
            assert expected_text in alert_text
            alert.accept()
        except:
            alert_text = email_input.get_attribute("validationMessage")
            print("Validation Message:", alert_text)

            # Assert validation message
        assert expected_text in alert_text, f"Validation failed! Found: {alert_text}"













