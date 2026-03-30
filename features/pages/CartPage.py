from selenium.webdriver.common.by import By
from .BasePage import BasePage
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from select import *
from selenium.webdriver.support.ui import Select

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    # sub_total_xpath = "//div[@class='col-sm-4 col-sm-offset-8']//table/tbody/tr/td[2]"
    # exo_tax_xpath = "//div[@class='col-sm-4 col-sm-offset-8']//table/tbody/tr[2]/td[2]"
    checkout_link_text = "Checkout"
    coupon_code_dropdown_link_text = "Use Coupon Code"
    coupon_text_box_id = "input-coupon"
    coupon_button_id= "button-coupon"
    # coupon_warning_xpath = "//div[contains(text(), ' Warning: Coupon')]"
    estimate_dropdown_xpath = "//div/h4/a[contains(text(), 'Estimate Shipping')]"
    estimate_postcode_id = "input-postcode"
    popup_button_name = "shipping_method"
    popup_apply_button_id = "button-shipping"
    get_quotes_xpath = "//button[contains(text(), 'Get Quotes')]"

    use_certificate_xpath="//a[contains(text(), 'Use Gift Certificate')]"
    use_certificate_text_xpath = "//input[@id='input-voucher']"
    use_certificate_button_xpath = "//input[@id='button-voucher']"
    use_certificate_message_xpath = "//div[contains(text(), ' Warning: Gift Certificate')]"

    update_button_xpath = "//button[@type='submit']"
    update_success_xpath = "//div[contains(text(), 'Success: You have')]"

    remove_button_xpath = "//button[@class='btn btn-danger']"
    empty_message_xpath = "//div[@id='content']/p[contains(text(), 'Your shopping')]"

    continue_link_text = "Continue"

    continue_shopping_xpath = "//a[contains(text(), 'Continue Shopping')]"


    def cart_page_title(self):
        assert "Shopping Cart" in self.driver.title

    def verify_total_amount(self):
        table_header = self.driver.find_element(By.XPATH, "//div[@class='col-sm-4 col-sm-offset-8']//table/tbody")

        sub_total = table_header.find_element(By.XPATH, ".//tr/td[2]").text
        sub_total = sub_total.replace("$", "")
        eco_tax = table_header.find_element(By.XPATH, ".//tr[2]/td[2]").text
        eco_tax = eco_tax.replace("$", "")
        vat = table_header.find_element(By.XPATH, ".//tr[3]/td[2]").text
        vat = vat.replace("$", "")
        total_value = table_header.find_element(By.XPATH, ".//tr[4]/td[2]").text
        total_value = total_value.replace("$", "")

        sub_total = float(sub_total)
        eco_tax = float(eco_tax)
        vat = float(vat)
        total_value = float(total_value)

        expected_total = sub_total + eco_tax + vat

        assert expected_total == total_value

    def checkout_cart_items(self):
        self.click_on_element("checkout_link_text", self.checkout_link_text)

    def click_coupon_dropdown(self):
        self.click_on_element("coupon_code_dropdown_link_text", self.coupon_code_dropdown_link_text )

    def enter_coupon_code(self,coupon_text):
        self.send_text_to_element("coupon_text_box_id", self.coupon_text_box_id, coupon_text)



    def click_coupon_button(self):
        self.click_on_element("coupon_button_id", self.coupon_button_id)

    def warning_message(self):
        wait = WebDriverWait(self.driver, 20)
        warning=wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(text(), ' Warning: Coupon')]")))
        return warning.text.strip()

    def estimate_dropdown(self):
        self.click_on_element("estimate_dropdown_xpath", self.estimate_dropdown_xpath)

    def estimate_country_dropdown(self):
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(expected_conditions.visibility_of_element_located((By.ID, "input-country")))
        #wait until enabled
        #wait.until(lambda driver: dropdown.is_enabled())
        select = Select(dropdown)
        select.select_by_visible_text("India")

    def estimate_region(self):
        wait = WebDriverWait(self.driver, 10)
        region_dropdown = wait.until(expected_conditions.visibility_of_element_located((By.ID, "input-zone")))
        # region_dropdown = self.driver.find_element(By.ID, "input-zone")
        select = Select(region_dropdown)
        select.select_by_visible_text("Delhi")

    def estimate_postcode(self, postcode_text):
        self.send_text_to_element("estimate_postcode_id", self.estimate_postcode_id, postcode_text)

    def get_quotes_button(self):
        self.click_on_element("get_quotes_xpath", self.get_quotes_xpath)

    def popup(self):
        self.click_on_element("popup_button_name", self.popup_button_name)

    def popup_button(self):
        self.click_on_element("popup_apply_button_id", self.popup_apply_button_id)



    def success_message(self):
        wait = WebDriverWait(self.driver, 10)
        warning = wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Success: Your shipping')]")))
        return warning.text.strip()

    def use_certificate_dropdown(self):
        self.click_on_element("use_certificate_xpath", self.use_certificate_xpath)

    def use_certificate_text_box(self, code):
        self.send_text_to_element("use_certificate_text_xpath", self.use_certificate_text_xpath, code)


    def use_certificate_apply_button(self):
        self.click_on_element("use_certificate_button_xpath", self.use_certificate_button_xpath)

    def use_certificate_warning(self):
        error_message = self.driver.find_element(By.XPATH, self.use_certificate_message_xpath).text
        assert "Warning: Gift Certificate is either invalid" in error_message


    def verify_update_button(self):
        self.click_on_element("update_button_xpath", self.update_button_xpath)

    def verify_update_message(self):
        expected_message=self.driver.find_element(By.XPATH, self.update_success_xpath).text
        assert "You have modified" in expected_message

    def click_remove_button(self):
        self.click_on_element("remove_button_xpath", self.remove_button_xpath)

    def empty_cart_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.empty_message_xpath)))
        expected_text=self.driver.find_element(By.XPATH, self.empty_message_xpath).text
        assert "Your shopping cart" in expected_text

    def click_continue(self):
        self.click_on_element("continue_link_text", self.continue_link_text)


    def click_continue_shopping(self):
        self.click_on_element("continue_shopping_xpath", self.continue_shopping_xpath)



