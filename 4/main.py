import itertools
from typing import List, Set

class Board:
    def __init__(self, values: List[List[int]]):
        self.values = values
        self.marked: Set[(int, int)] = set()

    def mark(self, number: int):
        for i, row in enumerate(self.values):
            for j, value in enumerate(row):
                if value == number:
                    self.marked.add((i, j))

    def winning(self) -> bool:
        for i in range(len(self.values)):
            if self.winning_row(i):
                return True

        for j in range(len(self.values[0])):
            if self.winning_column(j):
                return True

        return False

    def winning_row(self, i: int) -> (int, bool):
        for j in range(len(self.values[0])):
            if (i, j) not in self.marked:
                return False
        return True

    def winning_column(self, j: int) -> bool:
        for i in range(len(self.values)):
            if (i, j) not in self.marked:
                return False
        return True

    def sum_unmarked(self) -> int:
        sum_: int = 0
        for i in range(len(self.values)):
            for j in range(len(self.values[0])):
                if (i, j) not in self.marked:
                    sum_ += self.values[i][j]
        return sum_

    def __repr__(self) -> str:
        output = ""
        for i, row in enumerate(self.values):
            for j, value in enumerate(row):
                if (i, j) in self.marked:
                    output += f'\033[1m{value}\033[0m\t'
                else:
                    output += f'{value}\t'
            output += '\n'
        return output

def part_one(numbers_drawn, boards):
    for drawn in numbers_drawn:
        for i, board in enumerate(boards):
            board.mark(drawn)
            if board.winning():
                print(board.sum_unmarked() * drawn)
                print(board)
                return

def part_two(numbers_drawn, boards):
    last_drawn = -1
    last_board = None
    for drawn in numbers_drawn:
        new_boards = []
        for board in boards:
            board.mark(drawn)
            if not board.winning():
                new_boards.append(board)
            else:
                last_drawn = drawn
                last_board = board
        boards = new_boards

    print(last_board.sum_unmarked() * last_drawn)
    print(last_board)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        # first line is numbers drawn
        numbers_drawn = map(int, f.readline().split(','))

        # then bingo squares
        boards: List[Board] = []
        n = 5
        while True:
            blank_line = f.readline()  # a blank line separates each square
            if not blank_line:
                break

            lines = []
            for _ in range(n):
                line = f.readline().split()
                lines.append(list(map(int, line)))
            boards.append(Board(lines))

    part_one(numbers_drawn, boards)
    part_two(numbers_drawn, boards)
