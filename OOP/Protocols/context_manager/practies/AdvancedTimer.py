from typing import Optional
from time import perf_counter, sleep


class AdvancedTimer:
    def __init__(self):
        self._last_run = None
        self._runs = []

    @property
    def min(self) -> Optional[float]:
        try:
            min_time = min(self._runs)
        except ValueError:
            return None
        return min_time

    @property
    def max(self) -> Optional[float]:
        try:
            max_time = max(self._runs)
        except ValueError:
            return None
        return max_time

    @property
    def last_run(self) -> Optional[float]:
        return self._last_run

    @property
    def runs(self) -> Optional[list]:
        return self._runs

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return True
        self._last_run = perf_counter() - self.start
        self._runs.append(self._last_run)
        return False


timer = AdvancedTimer()

with timer:
    sleep(1.5)

with timer:
    sleep(0.7)

with timer:
    sleep(1)

print([round(runtime, 1) for runtime in timer.runs])
print(round(timer.min, 1))
print(round(timer.max, 1))
