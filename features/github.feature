# Created by Admin at 28-03-2023
Feature: GitHub api validation
  # Enter feature description here

  Scenario: Session management check
   Given I have GitHub credentials
   When I hit getRepo api of github
   Then Status code of response should be 200
    # Enter steps here