from random import shuffle

class Card:

#	value = [2,3,4,5,6,7,8,9,10,J,K,Q,A]
#	suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	def __init__(self):
		values = [2,3,4,5,6,7,8,9,10,"Jack","King","Queen","Aces"]
		suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
		self.cards = [Card(value, suit) for suit in suits for value in values]


	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		count = self.count()
		actual = min([count, num])
		if count ==0:
			raise ValueError("All cards have been dealt")
		self.cards[-actual:]
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards
		# print(f"Going to remove {actual} cards")

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self,hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)



d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(hand)
print(d.cards)
#	print(d._deal(52))
#	print(d.count())
#	print(d._deal(3))

# d.cards.pop()
# print(d.count())


#	c = Card("A", "hearts")
#	c2 = Card("10", "Diamonds")
#	c3 = Card("K", "spades")
#	print(c)
#	print(c.suit)
#	print(c, c2, c3)