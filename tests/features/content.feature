Feature: Test that pages have correct content

  Scenario: Main page has a correct title
    Given I open url
    Then There is a title shown on the page
    And The title tag has content "Online Store | My Store"