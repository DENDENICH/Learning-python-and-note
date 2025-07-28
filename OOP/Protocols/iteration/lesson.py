
# Иетараторы - объекты, которые могут быть использованы в циклах for,
# т.е они являются производными от итерируемых объектов

# Итерируемый объект - объект (коллекция), который может быть преобразован в итератор

# Любой итератор является итерируемым объектом, но не наоборот

# Полезный сценарий использование итераторов:
# iter(callable, sentinel) -> iterator
# callable - функция, которая возвращает значение
# sentinel - значение, которое будет использоваться для остановки итерации. Некое стоп-значение возвращаемое из функции


# Простейший пример итератора, реализованого с помощью собственного класса

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

counter1 = Counter(3, 8)
for i in counter1:
    print(i)