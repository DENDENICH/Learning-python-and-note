

# Многоразовый - те объекты протокола контекстного менеджера, которые могут быть повторно использованы
# в других (не вложеных) контекстных менеджерах

### Пример

from time import perf_counter, sleep

class ReusableTimer:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = perf_counter() - self.start

timer = ReusableTimer()

with timer:
    sleep(1.5)
print('Затраченное время:', timer.elapsed)

with timer:
    sleep(0.7)
print('Затраченное время:', timer.elapsed)

with timer:
    sleep(1)
print('Затраченное время:', timer.elapsed)