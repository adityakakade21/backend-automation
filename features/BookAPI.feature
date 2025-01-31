# Created by Admin at 23-03-2023
Feature: Verify if Books are added and deleted using Library API

  @library
  Scenario: Verify AddBook functionality
    Given  the book details which need to be added in the Library
    When  when we execute AddBook PostAPI method
    Then  book is successfully added
    And status code of response should be 200

    @library
    Scenario Outline: Verify AddBook functionality
    Given  the book details with <isbn> and <aisle>
    When  when we execute AddBook PostAPI method
    Then  book is successfully added
      Examples:
       | isbn | aisle |
       | grger| 55677 |
       | uydf | 21233 |
