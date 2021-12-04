def part_one():
    prev_measurement = None
    num_increases = 0

    with open("input.txt", "r") as f:
        for line in f:
            measurement = int(line)
            if prev_measurement is not None and measurement > prev_measurement:
                num_increases += 1
            prev_measurement = measurement

    print(num_increases)


class Window:
    def __init__(self):
        self.value = 0
        self.num_measurements = 0

    def add_measurement(self, measurement):
        self.value += measurement
        self.num_measurements += 1

    def __repr__(self):
        return f'({self.value}, {self.num_measurements})'

def part_two():
    prev_measurement = None
    num_increases = 0
    window_counter = 0
    prev_windows = []

    with open("input.txt", "r") as f:
        for line in f:
            measurement = int(line)
            new_window = Window()
            prev_windows.append(new_window)

            for window in prev_windows:
                window.add_measurement(measurement)

            earliest_window = prev_windows[0]
            if earliest_window.num_measurements == 3:
                if prev_measurement is not None and earliest_window.value > prev_measurement:
                    num_increases += 1
                prev_measurement = earliest_window.value
                prev_windows = prev_windows[1:]

    print(num_increases)


if __name__ == '__main__':
    part_one()
    part_two()
