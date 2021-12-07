from typing import List, Optional


def solution_one_fuel_model(start: int, end: int) -> int:
    return abs(start - end)

def solution_two_fuel_model(start: int, end: int) -> int:
    n = abs(start - end)
    return n * (n+1) / 2

if __name__ == '__main__':
    starting_positions = List[int]
    with open('input.txt', 'r') as f:
        data = f.readline()
        starting_positions = list(map(int, data.split(',')))

    max_position: int = max(starting_positions)
    min_position: int = min(starting_positions)

    min_fuel_cost: Optional[int] = None
    for x in range(min_position, max_position + 1):
        fuel_cost: int = 0
        for p in starting_positions:
            fuel_cost += solution_two_fuel_model(x, p)
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost

    print(min_fuel_cost)
