from collections import defaultdict
from typing import Iterable, Dict


class FishCounter:
    _MAX_TIMER = 8

    def __init__(self, timers: Iterable[int]):
        self.counter: Dict[int] = defaultdict(int)
        for timer in timers:
            self.counter[timer] += 1


    def step(self):
        spawning = self.counter[0]
        self.counter[0] = 0
        for i in range(FishCounter._MAX_TIMER):
            self.counter[i] = self.counter[i+1]
        self.counter[FishCounter._MAX_TIMER - 2] += spawning
        self.counter[FishCounter._MAX_TIMER] = spawning


    def total(self) -> int:
        total: int = 0
        for i in range(FishCounter._MAX_TIMER + 1):
            total += self.counter[i]
        return total


if __name__ == '__main__':
    fishCounter: FishCounter
    DAYS = 256

    with open('input.txt', 'r') as f:
        l = f.readline()
        timers = map(int, l.split(','))
        fishCounter = FishCounter(timers)

    for _ in range(DAYS):
        fishCounter.step()

    print(fishCounter.total())
