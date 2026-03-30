@Regression
Feature: Login Functionality

  @login
  Scenario Outline: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |email                          |password     |
      |john3456@gmail.com             | 12345       |

  @invalid-login
  Scenario Outline: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email "<email>" and valid password say "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
      |email                          |password     |
      |john897@gmail.com              | 12345       |

  @invalid-password
  Scenario Outline: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email say "<email>" and invalid password say "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
    |email                            |password   |
    |amotoriapril2023sample@gmail.com |1234567890 |

  @invalid-cred
  Scenario Outline: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email "<email>" and invalid password say "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
    |email                            |password   |
    |amotoriaprilsample@gmail.com     |1234567890 |

  @nologin-cred
  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning message


  Scenario: Verify forget password link
    Given I navigated to Login page
    When I click forget password link
    And I navigated to Forget password page
    Then I enter invalid email address
    And I click on continue button on forget password page
    Then I should see the warning message


  @empty-login-cred
  Scenario: Verify forget password link
    Given I navigated to Login page
    When I click forget password link
    And I navigated to Forget password page
    Then I enter valid email address
    And I click on continue button on forget password page
    Then I should see the success message on login page



