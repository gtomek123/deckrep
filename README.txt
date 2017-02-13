To run the program, go to the repository directory in command prompt and type
python deck.py
To run the tests, type
python decktest.py

The instructions for this project were to test only the code that determines the highest scoring hand.
As such, I am assuming that the API works flawlessly. Under other circumstances, I would feel inclined to test the values returned by the API. Some potential areas would be 1- failure of the API to return anything (connection issues) 2- faulty or ill-formatted data returned from API, 3- empty or null hands, 4- duplicate cards (easily possible given the APIs ability to handle multiple decks) 5- cards that could be wild (although this could also be handled outside of the API.)

Since I know that the values are being sorted, I made sure that the test data set includes hands that are not already in order. I also know that Straights that include Aces are treated differently depending on if the Ace is high or low, so tests are included for this. I also know that 0, J, Q, K were changed to numbers (or 10 for 0) for sorting purposes, so I made sure some tests include those cards. Aside from these cases, there is not much else to do except test each kind of hand. 

Due to the way five card poker works, hands that can fulfill more than one type of hand are fairly limited. For example, a hand could be a Flush and a High Card hand, so you need to check for the flush first. If you were playing seven card poker, there would be a lot more opportunity for hands that could fulfill multiple types of hands. For example, 3H, 4H, 5H, 6H, 7S, 8S, 9H is both a straight and a flush but not a straight flush. Testing for seven card poker would include several more cases like this.