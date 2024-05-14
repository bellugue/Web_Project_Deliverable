Feature: Register User
    In order to being able to create new users
    I want to register a user with its details

Scenario: Register a new User
    When I register a new user
      | username | email        | password   | password2   |
      | admin    | admin@adm.in | mypassword1 | mypassword1 |
    Then I'm viewing the main page