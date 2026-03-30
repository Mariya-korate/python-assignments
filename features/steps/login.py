from datetime import datetime
from behave import *
from selenium.webdriver.common.by import By
from features.pages.HomePage import HomePage



@given(u'I navigated to Login page')
def step_impl(context):
    # creating Home Page object
   context.home = HomePage(context.driver)
   context.home.click_on_my_account()
   assert context.home.check_home_page_title("Your Store")
   # Getting login page object from the function call
   context.login = context.home.select_login_option()



@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context,email,password):
    context.login.enter_email_address(email)
    context.login.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.login.click_on_login_button()

@then(u'I should get logged in')
def step_impl(context):
    warning_message = "Edit your account information"
    assert context.login.display_status_of_warning_message(warning_message)



@when(u'I enter invalid email "{email}" and valid password say "{password}" into the fields')
def step_impl(context,email,password):
    # context.login.enter_email_address("john897@gmail.com")
    # context.login.enter_password("12345")
    context.login.enter_email_address(email)
    context.login.enter_password(password)


# Assignment: Refactor this code
@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]") \
     .text.__contains__(expected_warning_message)




@when(u'I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context,email,password):
    context.login.enter_email_address(email)
    context.login.enter_password(password)


@when(u'I enter invalid email "{email}" and invalid password say "{password}" into the fields')
def step_impl(context,email,password):
    context.login.enter_email_address(email)
    context.login.enter_password(password)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login.enter_email_address("")
    context.login.enter_password("")


@when(u'I click forget password link')
def step_impl(context):
    context.login.forget_password()


@when(u'I navigated to Forget password page')
def step_impl(context):
    context.login.forget_password_page()


@then(u'I enter invalid email address')
def step_impl(context):
    input_email = "john897@gmail.com"
    context.login.forget_password_input(input_email)

@then(u'I should see the warning message')
def step_impl(context):
    context.login.forget_password_email_notfound()

@then(u'I click on continue button on forget password page')
def step_impl(context):
    context.login.click_forget_continue_button()


@then(u'I enter valid email address')
def step_impl(context):
    valid_email = "mk.korate@gmail.com"
    context.login.forget_password_input(valid_email)




@then(u'I should see the success message on login page')
def step_impl(context):
    context.login.forget_email_success()


# @when('I enter email "{email}" and password "{password}"')
# def step_impl(context,email,password):
#     email = email.strip()
#     password = password.strip()
#
#     print(f"Email: '{email}' | Password: '{password}'")
#     context.login.enter_email_address(email)
#     context.login.enter_password(password)



