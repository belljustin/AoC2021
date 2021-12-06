from collections import Counter
from typing import List, Tuple


class Line:
    def __init__(self, p1: Tuple[int, int], p2: Tuple[int, int]):
        self.p1 = p1
        self.p2 = p2


    def covers(self) -> List[Tuple[int]]:
        ret: List[Tuple[int, int]] = []

        if self.p1[0] == self.p2[0]:
            # vertical
            x = self.p1[0]

            if self.p1[1] > self.p2[1]:
                upper_y = self.p1[1]
                lower_y = self.p2[1]
            else:
                upper_y = self.p2[1]
                lower_y = self.p1[1]

            for y in range(lower_y, upper_y + 1):
                ret.append((x, y))

        elif self.p1[1] == self.p2[1]:
            # horizontal
            y = self.p1[1]

            if self.p1[0] > self.p2[0]:
                upper_x = self.p1[0]
                lower_x = self.p2[0]
            else:
                upper_x = self.p2[0]
                lower_x = self.p1[0]

            for x in range(lower_x, upper_x + 1):
                ret.append((x, y))

        else:
            if self.p1[0] < self.p2[0]:
                lower_x = self.p1[0]
                upper_x = self.p2[0]

                starting_y = self.p1[1]
                ending_y = self.p2[1]
            else:
                lower_x = self.p2[0]
                upper_x = self.p1[0]

                starting_y = self.p2[1]
                ending_y = self.p1[1]

            y = starting_y
            if starting_y < ending_y:
                inc = 1
            else:
                inc = -1
            for x in range(lower_x, upper_x + 1):
                ret.append((x, y))
                y += inc

        return ret

    def __repr__(self) -> str:
        return f'{self.p1[0]},{self.p1[1]} -> {self.p2[0]},{self.p2[1]}'


if __name__ == '__main__':
    lines: List[Line] = []

    with open('input.txt', 'r') as f:
        for l in f:
            l_split = l.split(' -> ')
            assert len(l_split) == 2
            p1 = l_split[0].split(',')
            p2 = l_split[1].split(',')

            p1 = (int(p1[0]), int(p1[1]))
            p2 = (int(p2[0]), int(p2[1]))

            lines.append(Line(p1, p2))

    c = Counter()
    overlaps = 0
    for l in lines:
        for occupied in l.covers():
            c[occupied] += 1
            if c[occupied] == 2:
                overlaps += 1

    print(overlaps)
