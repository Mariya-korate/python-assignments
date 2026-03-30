from behave import *
from selenium.webdriver.common.by import By
from datetime import datetime
from features.pages.HomePage import HomePage


@given(u'I navigate to Register Page')
def step_impl(context):
    # context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    # context.driver.find_element(By.LINK_TEXT, "Register").click()
    context.home = HomePage(context.driver)
    context.home.click_on_my_account()
    assert context.home.check_home_page_title("Your Store")
    context.register=context.home.navigate_register_page()

@when(u'I enter the below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        first_name = row['first_name']
        last_name = row['last_name']
        telephone = row['telephone']
        password = row['password']

        context.register.register_first_name(first_name)
        context.register.register_last_name(last_name)
        context.register.register_email_id()
        context.register.register_telephone(telephone)
        context.register.register_password(password)
        context.register.register_password_confirm(password)

    # print(f"DEBUG: Entered existing email -> {email_used}")

@when(u'I enter the below details and existing email id')
def step_impl(context):
    for row in context.table:
        first_name = row['first_name']
        last_name = row['last_name']
        telephone = row['telephone']
        password = row['password']

        context.register.register_first_name(first_name)
        context.register.register_last_name(last_name)
        # context.register.register_email_id()
        context.register.register_telephone(telephone)
        context.register.register_password(password)
        context.register.register_password_confirm(password)

@when(u'I enter below details into mandatory fields')
def step_impl(context):

    # context.driver.find_element(By.ID, "input-firstname").send_keys("John")
    # context.driver.find_element(By.ID, "input-lastname").send_keys("Mathew")
    # time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # new_email = "johnmathew"+time_stamp+"@gmail.com"
    # context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    # context.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    # context.driver.find_element(By.ID, "input-password").send_keys("12345")
    # context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
    for row in context.table:
        first_name = row['first_name']
        last_name = row['last_name']
        email_id = row['email_id']
        telephone = row['telephone']
        password = row['password']

        context.register.register_first_name(first_name)
        context.register.register_last_name(last_name)
        # context.register.register_email()
        context.register.register_email(email_id)
        context.register.register_telephone(telephone)
        context.register.register_password(password)
        context.register.register_password_confirm(password)

    # print(f"DEBUG: Entered existing email -> {email_used}")



@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register.register_agree()


@when(u'I click on Continue button')
def step_impl(context):
    # context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    context.register.register_continue()

@then(u'Account should get created')
def step_impl(context):
    # expected_text = "Your Account Has Been Created!"
    # assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(expected_text)
    context.register.account_created()

# @when(u'I enter below details into all fields')
# def step_impl(context):
#     pass

@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.register.existing_email()


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    context.register.email_already_registered()


# @when(u'I dont enter anything into the fields')
# def step_impl(context):
#     for row in context.table:
#         first_name = row['first_name']
#         last_name = row['last_name']
#         telephone = row['telephone']
#         password = row['password']
#
#         context.register.register_first_name(first_name)
#         context.register.register_last_name(last_name)
#         # context.register.register_email()
#         context.register.register_telephone(telephone)
#         context.register.register_password(password)
#         context.register.register_password_confirm(password)

@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    context.register.first_name_warning("First Name must be between 1 and 32 characters!")
    context.register.last_name_warning("Last Name must be between 1 and 32 characters!")
    context.register.email_warning("E-Mail Address does not appear to be valid!")
    context.register.telephone_warning("Telephone must be between 3 and 32 characters!")
    context.register.password_warning("Password must be between 4 and 20 characters!")

@then(u'Proper warning messages for first_name field should be displayed')
def step_impl(context):
    context.register.first_name_warning("First Name must be between 1 and 32 characters!")

@then(u'Proper warning messages for last_name field should be displayed')
def step_impl(context):
    context.register.last_name_warning("Last Name must be between 1 and 32 characters!")


@then(u'Proper warning messages for email field should be displayed')
def step_impl(context):
    context.register.email_warning("E-Mail Address does not appear to be valid!")

@then(u'Proper warning messages for telephone field should be displayed')
def step_impl(context):
    context.register.telephone_warning("Telephone must be between 3 and 32 characters!")


@then(u'Proper warning messages for password field should be displayed')
def step_impl(context):
    context.register.password_warning("Password must be between 4 and 20 characters!")

@when(u'I enter email without @')
def step_impl(context):
    context.register.email_without_at()

@then(u'Proper alert for the email_id should be displayed')
def step_impl(context):
   context.register.email_alert()



