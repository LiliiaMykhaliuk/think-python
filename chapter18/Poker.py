'''
Exercises of the book "Think python"
18.12.3 Exercise:
'''

# The goal of these exercises is to estimate the probability of drawing these various hands.
# 
# 1. Download the following files from http://thinkpython2.com/code:
# Card.py
# : A complete version of the Card, Deck and Hand classes in this chapter.
# PokerHand.py
# : An incomplete implementation of a class that represents a poker hand, and some code that tests it.
# 
# 2. If you run PokerHand.py, it deals seven 7-card poker hands and checks to see if any of them
#    contains a flush. Read this code carefully before you go on.
# 3. Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True or False according
#    to whether or not the hand meets the relevant criteria. Your code should work correctly for “hands”
#    that contain any number of cards (although 5 and 7 are the most common sizes).
# 4. Write a method named classify that figures out the highest-value classification for a hand and sets
#    the label attribute accordingly. For example, a 7-card hand might contain a flush and a pair;
#    it should be labeled “flush”.
# 5. When you are convinced that your classification methods are working, the next step is to estimate
#    the probabilities of the various hands. Write a function in PokerHand.py that shuffles a deck of cards,
#    divides it into hands, classifies the hands, and counts the number of times various classifications appear.
# 6. Print a table of the classifications and their probabilities. Run your program with larger and larger
#    numbers of hands until the output values converge to a reasonable degree of accuracy.
#    Compare your results to the values at http://en.wikipedia.org/wiki/Hand_rankings.
# Solution: http://thinkpython2.com/code/PokerHandSoln.py.


from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1


    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1   


    def get_ranks_of_cards(self):
        """Returns sorted list of ranks of cards in a PlayerHand"""

        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        return sorted(ranks)


    def has_sequence_of_ranks(self, k, n):
        """Returns True if hand has n-sequences of k- ranks, False otherwise.

        k: amount of same ranks in sequence
        n: amount of sequences in hand
        """

        # Make a histogram for ranks in cards
        self.rank_hist()

        # Check for sequence of cards
        pair = 0
        for rank_cards in self.ranks.values():
            # If the histogram has k - amount of cards with the same rank
            if rank_cards >= k:
                pair += 1

            # If the histogram has n - times k - amount of cards with same rank
            if pair == n:
                return True
        return False



    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""

        return self.has_sequence_of_ranks(2, 1)


    def has_two_pair(self):
        """Returns True if the hand has two_pair, False otherwise."""

        return self.has_sequence_of_ranks(2, 2)


    def has_three_of_a_kind(self):
        """Returns True if the hand has a three_of_a_kind, False otherwise."""

        return self.has_sequence_of_ranks(3, 1)


    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise."""

        # Get ranks of all cards in sorted list
        sorted_rank = self.get_ranks_of_cards()

        return has_5_ranks_in_row(sorted_rank)


    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
     
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


    def has_full_house(self):
        """Returns True if the hand has a full_house, False otherwise.
           (full_house is 3 cards with one rank, 2 cards with another)
        """
        # Make a histogram for ranks in cards
        self.rank_hist()

        found_3 = 0
        found_2 = 0
        # Go through histogram of ranks
        for rank_cards in self.ranks.values():

            # Found 3 cards with same rank
            if rank_cards >= 3 and found_3 == 0:
                found_3 = 1
                continue

            # Found 2 cards with same rank
            if rank_cards >= 2 and found_2 == 0:
                found_2 = 1
                continue

        # If we got full house
        if found_2 == 1 and found_3 == 1:
            return True
        return False


    def has_four_of_a_kind(self):
        """Returns True if the hand has a four_of_a_kind, False otherwise."""

        return self.has_sequence_of_ranks(4, 1)

    
    def has_straight_flush(self):
        """Returns True if the hand has a straight_flush, False otherwise."""

        # Make {suit : [ranks]} dictionary
        suits_ranks = {}
        for card in self.cards:
            suits_ranks.setdefault(card.suit, [])
            suits_ranks[card.suit].append(card.rank)
        
        # Go through each suit to see if any suit got sequence of 5 ranks
        for ranks in suits_ranks.values():
            sorted_ranks = sorted(ranks)

            if has_5_ranks_in_row(sorted_ranks):
                return True
        return False


    def classify(self):
        """Returns the highest-value label attribute in current PokerHand"""

        # Set priorities for labels
        labels_priority = ['straight flush', 'four of a kind', 'full house', 'flush', 'straight', 'three of a kind', 'two pair', 'pair']
        # Set functions according to priority
        labels_functions = [
            self.has_straight_flush(),
            self.has_four_of_a_kind(),
            self.has_full_house(),
            self.has_flush(),
            self.has_straight(),
            self.has_three_of_a_kind(),
            self.has_two_pair(),
            self.has_pair()
        ]

        # Check for labels in PokerHand in decreasing order
        label = ''
        for label_class in range(8):
            if labels_functions[label_class]:
                label = labels_priority[label_class]
                break
        return label



def has_5_ranks_in_row(rank_list):
    """Return True if list has sequence of 5 cards in a row.
       (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)

       rank_list: sorted list of ranks
    """

    amount_in_sequence = 0

    last_index = len(rank_list) - 1
    for index, rank in enumerate(rank_list):

        # [10-Jack-Queen-King-Ace] case
        if amount_in_sequence == 3 and rank == 13 and rank_list[0] == 1:
            return True
    
        # Break if there are no more items
        if index + 1 > last_index:
            break

        # Check if current rank is less than next one
        if rank_list[index + 1] - rank == 1:
            amount_in_sequence += 1
        else:
            amount_in_sequence = 0

        # In case we have straight (5 ranks in a row)
        if amount_in_sequence == 4:
            return True
    return False


def deal_hands(deck_cards, amount_of_hands, amount_of_cards_per_hand):
    """Create the appropriate number of PokerHand objects. Deal the appropriate number of cards per hand.
    amount_of_hands: amount of hands that have to be created
    amount_of_cards_per_hand: number of cards per hand

    return: list of Hands
    """

    deck_cards.shuffle()
    poker_hands_list = []

    # Create PokerCards
    for i in range(amount_of_hands):
        poker_hands_list.append(PokerHand())
        # Set cards to PokerHands
        deck_cards.move_cards(poker_hands_list[i], amount_of_cards_per_hand)

    return poker_hands_list


def count_classifications(poker_hands):
    """Classifies the hands, and counts the number of times various classifications appear"""

    count_classification = {}

    # Go through PokerHands
    for poker_hand in poker_hands:
        # Classify PokerHand
        classification = poker_hand.classify()
        # Count amount of classification
        if classification:
            count_classification[classification] = count_classification.get(classification, 0) + 1
    return count_classification


def run_cases(n):
    """Create the deck. Shuffles it. Deals PokerHands. Counts probability of classifications"""

    probabilities = {}

    # Deal hands n times
    for i in range(n):
        deck = Deck()
        hands = deal_hands(deck, 10, 5)
        classified_hands = count_classifications(hands)

        # Save classifications of hands in this case
        for label, counter in classified_hands.items():
            probabilities[label] = probabilities.get(label, 0) + counter

    # Count probability of each classification
    for classification, amount in probabilities.items():
        probabilities[classification] = (amount * 100) / (n * 10)
    return probabilities

if __name__ == '__main__':

    result = run_cases(100000)
    for label in sorted(result, key=result.get, reverse=True):
        print(f"{result[label]} % | {label}")
