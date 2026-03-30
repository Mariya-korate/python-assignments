from datetime import datetime
from behave import *
from selenium.webdriver.common.by import By
from features.pages.HomePage import HomePage

@given(u'I Select products from homepage')
def step_impl(context):
    context.home = HomePage(context.driver)
    assert context.home.check_home_page_title("Your Store")
    context.cart = context.home.click_on_product()
    # context.cart = context.home.product_add_to_cart()
    # context.cart = context.home.click_on_cart()
    # context.cart = context.home.click_on_view_cart()


@when(u'I add product to the cart')
def step_impl(context):
    context.cart = context.home.product_add_to_cart()




@when(u'I click on cart button')
def step_impl(context):
    context.cart = context.home.click_on_cart()



@when(u'I select the view cart from the popup')
def step_impl(context):
    context.cart = context.home.click_on_view_cart()



@when(u'I navigate to Cart Page')
def step_impl(context):
    context.cart.cart_page_title()


@then(u'I verify the total amount')
def step_impl(context):
    context.cart.verify_total_amount()



@then(u'I click checkout button')
def step_impl(context):
    context.cart.checkout_cart_items()


@when(u'I click use coupen code dropdown')
def step_impl(context):
    context.cart.click_coupon_dropdown()


@then(u'I enter coupen code as "{coupon_code}"')
def step_impl(context, coupon_code):
    context.cart.enter_coupon_code(coupon_code)

@then(u'I click on Apply coupen button')
def step_impl(context):
    context.cart.click_coupon_button()

@then(u'I should get a proper coupen warning message')
def step_impl(context):
    warning_text=context.cart.warning_message()
    expected_message="Warning: Coupon"
    assert expected_message in warning_text


@when(u'I click on estimate shipping and taxes dropdown')
def step_impl(context):
    context.cart.estimate_dropdown()

@then(u'I select country from dropdown')
def step_impl(context):
    context.cart.estimate_country_dropdown()

@then(u'I select region from dropdown')
def step_impl(context):
    context.cart.estimate_region()


@then(u'I enter postcode "{post_code}" in to the field')
def step_impl(context, post_code):
    context.cart.estimate_postcode(post_code)


@then(u'I click get quotes button')
def step_impl(context):
    context.cart.get_quotes_button()



@then(u'I select flate rate from popup')
def step_impl(context):
    context.cart.popup()


@then(u'I click Apply shipping button')
def step_impl(context):
    context.cart.popup_button()



@then(u'I can see the shipping estimate applied message')
def step_impl(context):
    success_text = context.cart.success_message()
    expected_message = "Success: Your shipping"
    assert expected_message in success_text

# Gift certificate
@when(u'I click on use gift certificate dropdown')
def step_impl(context):
    context.cart.use_certificate_dropdown()



@when(u'I enter "{code}" in the text field')
def step_impl(context, code):
    code = 1234
    context.cart.use_certificate_text_box(code)


@when(u'I click Apply Gift certificate button')
def step_impl(context):
    context.cart.use_certificate_apply_button()


@then(u'I should see the gift certificate warning message')
def step_impl(context):
    context.cart.use_certificate_warning()


@when(u'I click on update button')
def step_impl(context):
    context.cart.verify_update_button()


@then(u'I should see the update success message')
def step_impl(context):
    context.cart.verify_update_message()


@when(u'I click on remove icon')
def step_impl(context):
    context.cart.click_remove_button()


@then(u'I should see the empty shopping cart')
def step_impl(context):
    context.cart.empty_cart_message()


@then(u'I click on continue button')
def step_impl(context):
    context.cart.click_continue()
    home_page = HomePage(context.driver)
    return home_page


@then(u'I navigate to Home page')
def step_impl(context):
    context.home.navigate_home_page()

@when(u'I click on continue shopping button')
def step_impl(context):
    context.cart.click_continue_shopping()
    home_page = HomePage(context.driver)
    return home_page







