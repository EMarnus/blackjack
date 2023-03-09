import random

cards = []

suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

for suit in suits:
  for rank in ranks:
    cards.append([suit, rank])

def shuffle():
  random.shuffle(cards)


def deal(num):
  cards_dealt = []
  for _ in range(num):
    card = cards.pop()
    cards_dealt.append(card)
  return cards_dealt


shuffle()
cards_dealt = deal(2)

rank = cards_dealt[0][1]

if rank == "A":
  value = 11
elif rank == "J":
  value = 10
elif rank == "Q":
  value = 11
elif rank == "K":
  value = 12
else:
  value = rank

rank_dict = {"rank" : rank, "value" : value}

print(rank_dict["rank"], rank_dict["value"])