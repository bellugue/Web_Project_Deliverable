Feature: Create Car
    In order to add a new car to the dealership
    I want to fill in the car details and submit the form

Background:
    Given I have a user account with username "admin" and password "mypassword1"

Scenario: Add a new Car
    Given I log in as "admin" with password "mypassword1"
    When I add a new car
      | AuthorisedDealer | name     | licensePlate | model   | brand    | mileage |
      | Dealer1          | CarName  | ABC123       | ModelX  | BrandY   | 12345   |
    Then I'm viewing the home page
