import collections
import random

# создание класса
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchCards:
    """Колода карт"""
    _ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    _suits = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self._ranks for suit in self._suits]

    def __len__(self):
        """
        Для использование функции len с объектмо класса
        """
        return len(self._cards)

    def __getitem__(self, position: int):
        """
        Использование индексации (соответственно и итерирования) с объектом класса
        position - индекс
        """
        return self._cards[position]

french = FrenchCards()

# можно найти длину калоды
print(f'Длина - {len(french)}')

# индексироваться
print(f'Индексирование - {french[0]}')
print(f'Индексирование - {french[-3]}')

# выбирать рандомную
print(f'Рандомная - {random.choice(french)}')

french_reverse = random.choices(french, k=len(french))
print(f'Перетасованная - {french_reverse}')

# Срезы
french_player = french_reverse[:8:]
print(f'Срезы - {french_player}')

# Итерирование
for card in french_player:
    print(f'\tИтерирование - {card}')