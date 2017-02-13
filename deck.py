import json
import urllib.request
import statistics
from collections import Counter


def getShuffledDeck():
    #  creates a new shuffled deck, returns the deck_id
    req = urllib.request.Request(url='https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1', headers = {'User-Agent': 'Mozilla/5.0'}, method='GET')
    res = urllib.request.urlopen(req, timeout=5)
    adict = json.loads(res.read().decode('utf8'))
    deck_id = adict["deck_id"]
    return deck_id

def getHandFromDeck(deck_id):
    #  takes a deck id, returns a hand of 5 random cards from it
    req = urllib.request.Request(url='https://deckofcardsapi.com/api/deck/{0}/draw/?count=5' .format(deck_id), headers = {'User-Agent': 'Mozilla/5.0'}, method='GET')
    res = urllib.request.urlopen(req, timeout=5)
    adict2 = json.loads(res.read().decode('utf8'))
    myhand = []
    numcards = 5
    counter = 0
    while counter<numcards :
        myhand.append(adict2["cards"][counter]["code"])
        counter += 1
    return myhand

def isFlush(hand):
    #  takes a hand, returns Boolean - is it a Flush or not 
    suit = hand[0][1]
    if suit == hand[1][1] and suit == hand[2][1] and suit == hand[3][1] and suit == hand[4][1] :
        return True
    else :
        return False

def isStraight(numlist):
    #  takes a sorted list of numbers from a hand, returns Boolean - is it a Straight or not
    numlist = list(numlist)
    firstnum = numlist[0]
    if numlist[1] == firstnum + 1 and numlist[2] == firstnum + 2 and numlist[3] == firstnum + 3 and numlist[4] == firstnum + 4:
        return True
    #  this handles the Ace = 14 straight by checking if the hand is 1,10,11,12,13
    elif numlist[0] == 1 and numlist[1] == 10 and numlist[2] == 11 and numlist[3] == 12 and numlist[4] == 13:
        return True
    else :
        return False

def changeToNumsOnly(hand):
    #  takes a hand, returns a list of numbers from the hand
    #  for the purposes of a straight, an Ace could be a 1 or a 14
    #  here Ace is set to 1, the case involving 14 is handled in isStraight()
    nums = []
    for card in hand:
        if card[0] == "A":
            nums.append(1)
        elif card[0] == "0":
            nums.append(10)
        elif card[0] == "J":
            nums.append(11)
        elif card[0] == "Q":
            nums.append(12)
        elif card[0] == "K":
            nums.append(13)
        else :
            nums.append(int(card[0]))
    return nums

def sortHand(list):
    #  takes a number list, returns list sorted ascending
    return sorted(list)
   
def mostSecondMost(sortednumlist):
    #  takes a sorted list of just the numbers (no suit) of a hand
    #  returns just the counts (the number itself doesn't matter to determine the hand)
    #  of the most frequently occuring number and the second most frequently occuring number
    sortednumlist = list(sortednumlist)
    c = Counter(sortednumlist)
    most = c.most_common(2)[0][1]
    secondMost = c.most_common(2)[1][1]
    return (most, secondMost)

def whatHand(hand):
    #  takes a hand object and returns the name of its best Poker hand
    thenums = (changeToNumsOnly(hand))
    sortednums = (sortHand(thenums))
    mostSecondmostList = mostSecondMost(sortednums)
    if isFlush(hand):
        if isStraight(sortednums):
            return "Straight flush"
        else :
            return "Flush"
    elif isStraight(sortednums):
        return "Straight"
    elif mostSecondmostList == (4,1):
        return "Four of a kind"
    elif mostSecondmostList == (3,2):
        return "Full house"
    elif mostSecondmostList == (3,1):
        return "Three of a kind"
    elif mostSecondmostList == (2,2):
        return "Two pair"
    elif mostSecondmostList == (2,1):
        return "One pair"
    elif mostSecondmostList == (1,1):
        return "High card"    
    else :
        return ("Error, no hand found")

        
if __name__ == '__main__':
    deck_id = getShuffledDeck()
    myhand = getHandFromDeck(deck_id)
    print ("Your hand is", myhand)
    print ("The best poker hand that these cards fulfill is", whatHand(myhand))
