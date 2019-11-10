# Created by olegrakityanskiy at 11/9/19
Feature: Tests for Wholefood pages
  # Enter feature description here

  Scenario: Each Wholefood product has Regular price
    Given Open Wholefoods Deals page
    Then Each product has a regular price and name