Feature: Create a user given a name, a surname and a login

    As the admin
    I want insert a new login in the base
    Because I want to create a new user with a given login

    Scenario: The login is in wrong format
        Given I am on the insertion page
        When I insert a name, a surname and a wrong formatted login
        Then I can see an wrong format error message

    Scenario: The login is in correct format and the login doesn't already exist
        Given I am on the insertion page
        When I insert a name, a surname and a correct formatted login
        Then I can see the new created user

    Scenario: The login is in correct format but already exists in the system
        Given I am on the insertion page
        When I insert a name, a surname and a correct formatted login
        Then I can see an an user already exists error message

    Scenario: the value is correctly displayed for a man
        Given I am on the convertor page as a man
        When I enter a height value, and the man checkbox is checked and then validate
        Then I can see the corresponding weight for a man

    Scenario: the value is correctly displayed for a woman
        Given I am on the convertor page as a woman
        When I enter a height value, and the woman checkbox is checked and then validate
        Then I can see the corresponding weight for a woman

Feature: Create a user given a name and a surname
    As the admin
    I want insert a new login in the base
    Because I want to create a new user automatically

    Scenario: Plan A: The name is longer than 8 characters
        Given I am on the insertion page
        When I insert a name longer than 8 characters and a surname
        Then I can see the new user with the generated login

    Scenario: Plan A bis: The name is shorter than 8 characters
        Given I am on the insertion page
        When I insert a name shorter than 8 characters and a surname
        Then I can see the new user with the generated login

    Scenario: Plan B
        Given I am on the insertion page
        When I insert a name shorter than 8 characters and a surname
        Then I can see the new user with the generated login
