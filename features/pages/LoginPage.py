from selenium.webdriver.common.by import By
from .BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    forget_password_link_text = "Forgotten Password"
    forget_input_email_id = "input-email"
    forget_continue_button_xpath = "//input[@type = 'submit']"
    forget_email_success_xpath = "//div[contains(text(), 'An email with a')]"

    def enter_email_address(self,email_text):
        # self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_text)
        self.send_text_to_element("email_address_field_id", self.email_address_field_id, email_text)

    def enter_password(self,password_text):
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)
        self.send_text_to_element("password_field_id", self.password_field_id, password_text)

    def click_on_login_button(self):
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        self.click_on_element("login_button_xpath", self.login_button_xpath)

    def display_status_of_warning_message(self,expected_warning_text):
         return self.driver.find_element(By.LINK_TEXT, "Edit your account information").text.__eq__(expected_warning_text)

    def click_on_warning_message(self):
        expected_message=self.driver.find_element(By.XPATH, "//div[contains(text(), 'Warning: No match')]").text
        assert "Warning: No match" in expected_message


    def forget_password(self):
        self.click_on_element("forget_password_link_text", self.forget_password_link_text)

    def forget_password_page(self):
        forgot_heading = (By.XPATH, "//h1[contains(text(),'Forgot Your')]")
        expected_heading=WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(forgot_heading)).text
        # assert "Forget Your Password" in self.driver.title, f"Expected page title to contain 'Forget Your Password', got '{self.driver.title}'"
        assert "Forgot Your" in expected_heading

    def forget_password_input(self, input_email):
        self.send_text_to_element("forget_input_email_id", self.forget_input_email_id, input_email)

    def forget_password_email_notfound(self):
        expected_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Warning: The E-Mail Address was')]").text
        assert "not found" in expected_message

    def click_forget_continue_button(self):
        self.click_on_element("forget_continue_button_xpath", self.forget_continue_button_xpath)

    def forget_email_success(self):
        expected_warining = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, self.forget_email_success_xpath))).text
        assert "confirmation link" in expected_warining

