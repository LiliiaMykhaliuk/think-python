"""Module with unit tests for exercise 18.12.3 of the book Think Python"""

import unittest

from Poker import PokerHand
from Card import Card

class Test_Poker_classification(unittest.TestCase):
    """Test cases for methods of possible hands in in Poker"""

    def test_has_pair(self):
        """Tests method has_pair of class PokerHand

        Hint: pair - two cards with the same rank
        """

        poker_hand = PokerHand()

        # Test case True
        set_1 = [Card(0, 4), Card(1, 4), Card(0, 2)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_pair())

        # Test case False
        set_2 = [Card(0, 7), Card(1, 4), Card(0, 2)]
        poker_hand.cards = set_2
        self.assertFalse(poker_hand.has_pair())


    def test_has_two_pairs(self):
        """Tests method has_two_pairs of class PokerHand

        Hint: two pair - two pairs of cards with the same rank
        """

        poker_hand = PokerHand()

        # Test case True
        set_1 = [Card(0, 4), Card(1, 4), Card(0, 2), Card(3, 2), Card(3, 3)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_two_pair())

        # Test case False
        set_2 = [Card(0, 7), Card(1, 4), Card(0, 2)]
        poker_hand.cards = set_2
        self.assertFalse(poker_hand.has_two_pair())


    def test_has_three_of_a_kind(self):
        """Tests method has_three_of_a_kind of class PokerHand

        Hint: three of a kind - three cards with the same rank
        """

        poker_hand = PokerHand()

        # Test case True
        set_1 = [Card(0, 4), Card(1, 4), Card(3, 4), Card(3, 2), Card(3, 3)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_three_of_a_kind())

        # Test case False
        set_2 = [Card(0, 7), Card(1, 7), Card(0, 2)]
        poker_hand.cards = set_2
        self.assertFalse(poker_hand.has_three_of_a_kind())


    def test_has_straight(self):
        """Tests method has_straight of class PokerHand

        Hint: straight - five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight 
                         and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
        """

        poker_hand = PokerHand()

        # Test case True (Ace-2-3-4-5)
        set_1 = [Card(0, 3), Card(1, 2), Card(3, 5), Card(3, 4), Card(3, 1), Card(3, 9)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_straight())

        # Test case True (10-Jack-Queen-King-Ace)
        set_2 = [Card(0, 11), Card(1, 10), Card(3, 12), Card(3, 1), Card(3, 13), Card(3, 6)]
        poker_hand.cards = set_2
        self.assertTrue(poker_hand.has_straight())

        # Test case False (Queen-King-Ace-2-3 is not)
        set_3 = [Card(0, 3), Card(1, 2), Card(3, 12), Card(3, 1), Card(3, 13), Card(3, 6)]
        poker_hand.cards = set_3
        self.assertFalse(poker_hand.has_straight())


    def test_has_flush(self):
        """Tests method has_flush of class PokerHand

        Hint: flush - five cards with the same suit
        """

        poker_hand = PokerHand()

        # Test case True
        set_1 = [Card(0, 3), Card(0, 2), Card(0, 5), Card(0, 4), Card(0, 1), Card(3, 9)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_flush())

        # Test case False
        set_3 = [Card(0, 3), Card(1, 2), Card(0, 12), Card(0, 1), Card(0, 13), Card(3, 6)]
        poker_hand.cards = set_3
        self.assertFalse(poker_hand.has_flush())


    def test_has_full_house(self):
        """Tests method has_full_house of class PokerHand

        Hint: has_full_house - three cards with one rank, two cards with another
        """

        poker_hand = PokerHand()

        # Test case True
        set_1 = [Card(2, 3), Card(0, 3), Card(0, 5), Card(2, 5), Card(3, 5), Card(3, 9)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_full_house())

        # Test case False
        set_3 = [Card(0, 3), Card(1, 2), Card(0, 12), Card(0, 1), Card(0, 13), Card(3, 6)]
        poker_hand.cards = set_3
        self.assertFalse(poker_hand.has_full_house())


    def test_has_four_of_a_kind(self):
        """Tests method has_four_of_a_kind of class PokerHand

        Hint: has_four_of_a_kind - four cards with the same rank
        """
        poker_hand = PokerHand()

        # Test case True
        set_1 = [Card(2, 3), Card(1, 5), Card(0, 5), Card(2, 5), Card(3, 5), Card(3, 9)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_four_of_a_kind())

        # Test case False
        set_3 = [Card(0, 3), Card(1, 2), Card(0, 12), Card(0, 1), Card(0, 13), Card(3, 6)]
        poker_hand.cards = set_3
        self.assertFalse(poker_hand.has_four_of_a_kind())


    def test_has_straight_flush(self):
        """Tests method has_straight_flush of class PokerHand

        Hint: straight flush - five cards in sequence (as defined above) and with the same suit
        """

        poker_hand = PokerHand()

        # Test case True (Ace-2-3-4-5)
        set_1 = [Card(0, 3), Card(0, 2), Card(0, 5), Card(0, 4), Card(0, 1), Card(0, 9)]
        poker_hand.cards = set_1
        self.assertTrue(poker_hand.has_straight_flush)

        # Test case True (10-Jack-Queen-King-Ace)
        set_2 = [Card(1, 11), Card(1, 10), Card(1, 12), Card(1, 1), Card(1, 13), Card(1, 6)]
        poker_hand.cards = set_2
        self.assertTrue(poker_hand.has_straight_flush())

        # Test case False (Queen-King-Ace-2-3 is not)
        set_3 = [Card(2, 3), Card(2, 2), Card(2, 12), Card(2, 1), Card(2, 13), Card(2, 6)]
        poker_hand.cards = set_3
        self.assertFalse(poker_hand.has_straight_flush())



class Test_Poker_Get_highest_label(unittest.TestCase):
    """Test cases for methods of class PokerHand"""

    def test_classify(self):
        """Tests method classify of class PokerHand

        Hint: Method supposes to get highest classification in PokerHand
        """

        poker_hand = PokerHand()

        # straight flush > flush > pair
        set_1 = [Card(0, 3), Card(0, 2), Card(0, 5), Card(0, 4), Card(0, 1), Card(2, 9), Card(3, 9)]
        poker_hand.cards = set_1
        self.assertEqual(poker_hand.classify(), 'straight flush')

        # four of a kind > pair
        set_2 = [Card(1, 11), Card(0, 11), Card(1, 12), Card(1, 1), Card(3, 11), Card(2, 11)]
        poker_hand.cards = set_2
        self.assertEqual(poker_hand.classify(), 'four of a kind')

        # classification not found
        set_3 = [Card(2, 3), Card(3, 1), Card(2, 12), Card(2, 5), Card(3, 10), Card(1, 6)]
        poker_hand.cards = set_3
        self.assertEqual(poker_hand.classify(), '')


if __name__ == '__main__':
    unittest.main(verbosity=2)
