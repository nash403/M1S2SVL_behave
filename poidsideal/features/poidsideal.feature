Feature: get the perfect weight of a person given their height

    As a user of the convertor
    I want to convert height into perfect weight
    Because I want to know my perfect weight

    Scenario: The convertor page has a title
        When I am on the convertor page
        Then The right title is displayed

    Scenario: The convertor page has an input field
        When I am on the convertor page
        Then The page contains an input field

    Scenario: the convertor refuses the wrong data
        Given I am on the convertor page
        When I enter a non positive value
        Then I can see an error message

    Scenario: the value is correctly displayed for a man
        Given I am on the convertor page as a man
        When I enter a height value, and the man checkbox is checked and then validate
        Then I can see the corresponding weight for a man

    Scenario: the value is correctly displayed for a woman
        Given I am on the convertor page as a woman
        When I enter a height value, and the woman checkbox is checked and then validate
        Then I can see the corresponding weight for a woman
