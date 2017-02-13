import deck
import unittest

class TestWhatHand(unittest.TestCase):

    def test_Straight_Flush(self):
        self.assertEqual(deck.whatHand(['2D', '5D', '3D', '1D', '4D']), "Straight flush")
        self.assertEqual(deck.whatHand(['9H', '7H', '6H', '8H', '0H']), "Straight flush")
        self.assertEqual(deck.whatHand(['2D', '5D', '3D', '1D', '4D']), "Straight flush")
        self.assertEqual(deck.whatHand(['9S', 'JS', 'QS', '0S', 'KS']), "Straight flush")

    def test_Flush(self):
        self.assertEqual(deck.whatHand(['9D', '5D', '0D', 'QD', 'JD']), "Flush")

    def test_Straight(self):
        self.assertEqual(deck.whatHand(['1D', '2D', '3D', '4D', '5H']), "Straight")
        self.assertEqual(deck.whatHand(['7S', '0D', 'JD', '9D', '8H']), "Straight")
        self.assertEqual(deck.whatHand(['KD', 'AD', '0C', 'QD', 'JH']), "Straight")

    def test_Four_Of_A_Kind(self):
        self.assertEqual(deck.whatHand(['AH', 'AC', 'AS', '3D', 'AD']), "Four of a kind")
        self.assertEqual(deck.whatHand(['0H', 'JD', '0S', '0D', '0C']), "Four of a kind")

    def test_Full_House(self):
        self.assertEqual(deck.whatHand(['9D', 'JH', '9C', 'JD', 'JC']), "Full house")
        self.assertEqual(deck.whatHand(['KC', '3C', 'KD', 'KH', '3H']), "Full house")

    def test_Three_Of_A_Kind(self):
        self.assertEqual(deck.whatHand(['9D', '5C', '0D', '5H', '5D']), "Three of a kind")
        self.assertEqual(deck.whatHand(['9D', '5D', '9H', 'QD', '9S']), "Three of a kind")

    def test_Two_Pair(self):
        self.assertEqual(deck.whatHand(['0H', 'AC', '0D', 'AD', 'JS']), "Two pair")
        self.assertEqual(deck.whatHand(['8C', 'QD', '0D', 'QS', '8D']), "Two pair")

    def test_One_Pair(self):
        self.assertEqual(deck.whatHand(['9D', '5H', '0S', 'QD', '5C']), "One pair")
        self.assertEqual(deck.whatHand(['QH', '5C', '0D', 'QD', 'JH']), "One pair")

    def test_High_Card(self):
        self.assertEqual(deck.whatHand(['9H', '5D', 'KC', '2D', '0D']), "High card")
        self.assertEqual(deck.whatHand(['3S', '8C', '0D', 'QD', 'JS']), "High card")


if __name__ == '__main__':
    unittest.main()
