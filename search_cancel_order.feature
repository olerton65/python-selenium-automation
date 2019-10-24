# Created by olegrakityanskiy at 10/20/19
Feature:  Test Scenarios for Support Search functionality
  # Enter feature description here

  Scenario: User cagit addn search for solutions of order cancelling
    Given Open Amazon page1
    And Open Help page1
    When Input cancel order into search field1
    And Click on search icon1
    Then Product results for Cancel Items or Orders are shown1
