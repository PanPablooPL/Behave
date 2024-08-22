Feature: User logs in, adds a product to the cart, and verifies the cart

  Scenario: User logs in, adds a product to the cart, and verifies the cart
    Given I am on the homepage
    When I sign in
    And I add the first product to the cart
    Then I take a screenshot of the cart item
    And I log out
