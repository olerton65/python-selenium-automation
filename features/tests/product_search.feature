# Created by olegrakityanskiy at 10/19/19
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
    And Click Add to the cart btn
    And Close suggestion side section
    Then Verify cart has 1 item


  Scenario: User can add perfume Creed product to the cart
    Given Open Amazon page
    When Search for perfume Creed
    And Open the first product search result1
    And Select one-time purchase
    And Click Add to the cart btn
    And Close suggestion side section
    Then Verify cart has 1 item


    Scenario: User can open and close Today's deals under $25
      Given Open Amazon page
      When Store original windows
      And Click to open Deals under $25
      And Switch to the newly opened window
      Then Shop all deals are shown
      And User can close new window and switch back to original


  Scenario: User can add a product from today's deals
    Given Open Amazon page
    When Store original windows
    And Click to open Deals under $25
    And Switch to the newly opened window
    Then Shop all deals are shown
    And Click on the Book to add it to the cart
    And Click Add to the cart button
    And User can close new window and switch back to original
    And Refresh and verify cart has 1 item



