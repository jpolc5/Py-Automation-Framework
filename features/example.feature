Feature: Google Search
  As a user
  I want to search on Google
  So that I can find information

  Scenario: Perform a simple search
    Given I am on the Google homepage
    When I search for "Selenium with Python"
    Then I should see search results
