from enum import Enum

class Command(Enum):
    UP = 1
    DOWN = 2
    FORWARD = 3

class Submarine:
    def __init__(self):
        self.x = 0
        self.z = 0

    def take_command(self, command, value):
        assert isinstance(command, Command)
        if command == Command.UP:
            self.z -= value
        elif command == Command.DOWN:
            self.z += value
        elif command == Command.FORWARD:
            self.x += value

    def result(self):
        return self.x * self.z

class AimSubmarine:
    def __init__(self):
        self.x = 0
        self.z = 0
        self.aim = 0

    def take_command(self, command, value):
        assert isinstance(command, Command)
        if command == Command.UP:
            self.aim -= value
        elif command == Command.DOWN:
            self.aim += value
        elif command == Command.FORWARD:
            self.x += value
            self.z += self.aim * value

    def result(self):
        return self.x * self.z

def command_from_line(l):
    s_command, s_value = l.split()
    return Command[s_command.upper()], int(s_value)

if __name__ == '__main__':
    submarine = Submarine()
    aim_submarine = AimSubmarine()

    with open("input.txt", "r") as f:
        for l in f:
            command, value = command_from_line(l)
            submarine.take_command(command, value)
            aim_submarine.take_command(command, value)

    print(submarine.result())
    print(aim_submarine.result())
