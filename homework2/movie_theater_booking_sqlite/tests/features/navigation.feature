Feature: Navigate Booking App

Scenario: Navigate To And From The Landing Page
    Given I am at the Home page
    When I click the "Movies" button
    Then I will be brought to the "Movies" page
    When I click the "Return" button
    Then I will be brought to the "Home" page

    When I click the "Book Seat" button
    Then I will be brought to the "Book Seat" page
    When I click the "Return" button
    Then I will be brought to the "Home" page

    When I click the "Booking History" button
    Then I will be brought to the "Booking History" page
    When I click the "Return" button
    Then I will be brought to the "Home" page