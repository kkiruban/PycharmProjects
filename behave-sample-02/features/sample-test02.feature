# Created by kramasam at 4/10/20
# Created by kramasam at 4/10/20
@lms-user-creation
Feature: User registration
  As a new subscriber on LMS
  I want to be able to register myself with different user modes [Corporate User, Personal User, Corporate User with double byte information, Personal User with double byte information ]
  So that I can get my LMS account


  @behave_lms_qa
  Scenario: Create a new US personal user
    Given the base url is "https://training-lms-qa.redhat.com/sso/saml/auth/redhat"
    Given I open the url "https://training-lms-qa.redhat.com/sso/saml/auth/redhat"
    When I pause for 100ms
    Then I wait on element "#username"
    When I set "username" to the inputfield "#username"
    When I set "password" to the inputfield "#password"
#   When I click on the button "#_eventId_submit"
    When I click on button "#_eventId_submit" button
