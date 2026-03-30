@Regression
Feature: Cart functionality

  Background: I am on home page
    Given I Select products from homepage
    When I add product to the cart
    And I click on cart button
    And I select the view cart from the popup
    And I navigate to Cart Page

  Scenario: Add single product into cart and checkout
    Then I verify the total amount
    And I click checkout button


  Scenario: Add product into cart and use coupon code
    And I click use coupen code dropdown
    Then I enter coupen code as "1234"
    And I click on Apply coupen button
    Then I should get a proper coupen warning message


  Scenario: Estimate the shipping and taxes
    And I click on estimate shipping and taxes dropdown
    Then I select country from dropdown
    And I select region from dropdown
    And I enter postcode "567" in to the field
    And I click get quotes button
    And I select flate rate from popup
    And I click Apply shipping button
    Then I can see the shipping estimate applied message


  Scenario: Use Gift certificate
    And I click on use gift certificate dropdown
    And I enter "code" in the text field
    And I click Apply Gift certificate button
    Then I should see the gift certificate warning message

  Scenario: Verify the update icon on cart page
    And I click on update button
    Then I should see the update success message


  Scenario: Verify the remove icon on cart page
    And I click on remove icon
    Then I should see the empty shopping cart


  Scenario: Verify the continue button on cart page
    And I click on remove icon
    Then I should see the empty shopping cart
    And I click on continue button
    Then I navigate to Home page

  @cart
  Scenario: Verify continue shopping button on cart page
    And I click on continue shopping button
    Then I navigate to Home page



