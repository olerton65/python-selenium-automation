# Created by olegrakityanskiy at 11/3/19
Feature: Test for Amazon search functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for shoes
    Then Search results for shoes is shown


  Scenario: User can add printer paper product to the cart
    Given Open Amazon page
    When Search for printer paper
    And Open the first product search result
    And Click Add to the card button
    And Close suggestion side section
    Then Verify cart has 1 item


  Scenario: User can add perfume Creed product to the cart
    Given Open Amazon page
    When Search for perfume Creed
    And Open the first product search result1
    And Select one-time purchase
    And Click Add to the card button
    And Close suggestion side section
    Then Verify cart has 1 item
