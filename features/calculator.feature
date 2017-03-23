Feature: Calculator tests
	Scenario: Splash screen is loaded
		When upper text bar is: "Islam_Hamdy"
		And bottom text bar is: "Sarah Osama"
		Then ADD button should be present
		Then SUB button should be present

	Scenario: Verify ADD button works
		When user clicks ADD button
		Then upper text bar is: "Bravo ya islam"
		Then bottom text bar is: "new number =1"

	Scenario: Verifying addition is working
		When user clicks ADD button twice
		Then upper text bar is: "Bravo ya islam"
		Then bottom text bar is: "new number =2"

	Scenario: Verify SUB button works
		When user clicks SUB button
		Then upper text bar is: "Islam_hamdy"
		Then bottom text bar is: "new number =-1"

	Scenario: Verify subtraction is working
		When user clicks SUB button twice
		Then upper text bar is: "Islam_hamdy"
		Then bottom text bar is: "new number" =-2"



