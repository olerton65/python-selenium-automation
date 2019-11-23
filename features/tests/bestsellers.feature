# Created by olegrakityanskiy at 11/23/19
Feature: Test for Amazon links selection
  # Enter feature description here

  Scenario: Bestsellers links can be opened
    Given Open Amazon page
    When Open Amazon Bestsellers
    Then User can click through top links and verify correct page opens