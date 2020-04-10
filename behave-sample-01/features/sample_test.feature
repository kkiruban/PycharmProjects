# Created by kramasam at 4/10/20
@lms-user-creation
Feature: User registration
  As a new subscriber on LMS
  I want to be able to register myself with different user modes [Corporate User, Personal User, Corporate User with double byte information, Personal User with double byte information ]
  So that I can get my LMS account


  @browserstack_qa
  Scenario: Create a new US personal user
    Given I am on the "Login" page
    Then I should see "Log in to your Red Hat account"
    When I navigate to qa user registration page
    When I click on personal user radio button
