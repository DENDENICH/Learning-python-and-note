import array
# Генераторные выражения
symbols = 'regular'
ords = tuple(ord(symbol) for symbol in symbols)
array_ords = array.array('I', (ord(symbol) for symbol in symbols))
print(ords)
print(array_ords)


# Кортежи
# вывод кортежа
r = (5, 6)
print('%s <-> %s' % r)


# Сопоставление с образцом
def evaluate(arr):
    match arr:
        case ['one', _, _, res] if res > 20:
            return 1
        case ['two', _, _, res] if res == 20:
            return 2
        case ['three', _, _, (l, m) as coord] if isinstance(l, str) and isinstance(m, str):
            return coord
        case _:
            return False
print('\nСопоставление с образцом')
print(f'{['one', 'two', 'three', 10]} - {evaluate(['one', 'two', 'three', 10])}')
print(f'{['two', '/', ',', 20]} - {evaluate(['two', '/', ',', 20])}')
print(f'{['three', '1', '2', ('l', 'm')]} - {evaluate(['three', '1', '2', ('l', 'm')])}')
print(f'{['rt']} - {evaluate(['rt'])}')


# Срезы
# Именование срезов
print('\nСрезы')
slice1 = slice(0, 6)

for i in ['Hello world']:
    print(i[slice1])


