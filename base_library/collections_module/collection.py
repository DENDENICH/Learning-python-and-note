import collections

# создание класса
Card = collections.namedtuple('Card', ['rank', 'suit'])

card1 = Card(rank='7', suit='Q')
print(card1)