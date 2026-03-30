from selenium.webdriver.common.by import By
from .LoginPage import LoginPage
from .SearchPage import SearchPage
from .BasePage import BasePage
from .RegisterPage import RegisterPage
from .CartPage import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"
    register_option_link_text = "Register"
    #cart page
    product_link_text = "Tablets"
    product_add_to_cart_xpath = "//button/span[contains(text(), 'Add to Cart')]"
    click_cart_xpath = "//div[@id='cart']/button"
    view_cart_xpath = "//*[contains(text(), 'View Cart')]"


    def click_on_my_account(self):
        # self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        # self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        login_page = LoginPage(self.driver)
        return login_page

    def check_home_page_title(self, expected_title_text):
        return self.driver.title.__eq__(expected_title_text)

    # SearchPage
    def enter_product_into_search_box_field(self, product_text):
        # self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_text)
        self.send_text_to_element("search_box_field_name", self.search_box_field_name, product_text)

    def click_on_search_button(self):
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)

    #Register page

    def navigate_register_page(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        register_page = RegisterPage(self.driver)
        return register_page

    #cart page
    def click_on_product(self):
        self.click_on_element("product_link_text", self.product_link_text)

    def product_add_to_cart(self):
        self.click_on_element("product_add_to_cart_xpath", self.product_add_to_cart_xpath)

    def click_on_cart(self):
        # wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
        wait = WebDriverWait(self.driver, 20)
        cart=wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.click_cart_xpath)))

        # self.click_on_element("click_cart_xpath", self.click_cart_xpath)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart)
        cart = wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.click_cart_xpath))
        )
        self.driver.execute_script("arguments[0].click();", cart)

        # cart.click()

    def click_on_view_cart(self):
        self.click_on_element("view_cart_xpath", self.view_cart_xpath)
        cart_page = CartPage(self.driver)
        return cart_page


    # empty cart continue button
    def navigate_home_page(self):
        assert "Your Store" in self.driver.title