@Regression
Feature: Register Account functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter the below details into mandatory fields
        |first_name|last_name|telephone |password |
        |Arun      |Motoori  |1234567890|12345    |
    And I select Privacy Policy option
    And I click on Continue button
    Then Account should get created



#  Scenario: Register with all fields
#    Given I navigate to Register Page
#    When I enter below details into all fields
#        |first_name|last_name|telephone |password |
#        |Arun      |Motoori  |1234567890|12345    |
#    And I select Privacy Policy option
#    And I click on Continue button
#    Then Account should get created

  @existing-email
  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter the below details and existing email id
        |first_name|last_name|telephone |password |
        |John      |Mathew  |1234567890|12345     |
    And I enter existing accounts email into email field
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed

  @no-entry
  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I enter below details into mandatory fields
        |first_name|last_name |telephone  |password |email_id                 |
        |          |          |           |         |                         |
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning messages for every mandatory fields should be displayed


  Scenario: Register without providing first_name
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      |first_name | last_name | telephone  | password | email_id           |
      |            | Motoori   | 1234567890 | 12345    | mar@gmail.com   |
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning messages for first_name field should be displayed

  @all-scenario
   Scenario: Register without providing last_name
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      |first_name | last_name | email_id     |telephone  | password |
      |Arun       |           | mar@gmail.com|1234567890 | 12345    |
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning messages for last_name field should be displayed

   @all-sc
   Scenario: Register without providing last_name
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      |first_name | last_name | email_id     |telephone  | password |
      |Arun       | Tiwari    |              |1234567890 | 12345    |
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning messages for email field should be displayed

   @all-field
   Scenario: Register without providing last_name
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      |first_name | last_name | email_id     |telephone  | password |
      |Arun       | Tiwari    |mar@gmail.com |            | 12345    |
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning messages for telephone field should be displayed

   @all-field
   Scenario: Register without providing last_name
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      |first_name | last_name | email_id     |telephone  | password |
      |Arun       | Tiwari    |mar@gmail.com |1234567890 |          |
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning messages for password field should be displayed

    @all-field
   Scenario: Register without providing last_name
    Given I navigate to Register Page
    When I enter below details into mandatory fields
      |first_name | last_name | email_id     |telephone  | password |
      |Arun       | Tiwari    |mar@gmail.com |1234567890 |          |
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper warning messages for password field should be displayed

   @all-warning
   Scenario: Register without providing '@' in email field
    Given I navigate to Register Page
    When I enter email without @
    And I select Privacy Policy option
    And I click on Continue button
    Then Proper alert for the email_id should be displayed




