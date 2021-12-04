class BitCounter:
    def __init__(self, n):
        self.m = 0
        self.bit_counts = [0] * n

    def count(self, bits):
        self.m += 1
        for i in range(len(bits)):
            if bits[i] == '1':
                self.bit_counts[i] += 1

    def gamma(self):
        b_gamma = ""
        for c in self.bit_counts:
            if c > self.m/2:
                b_gamma += '1'
            else:
                b_gamma += '0'
        return int(b_gamma, 2)

    def epsilon(self):
        b_epsilon = ""
        for c in self.bit_counts:
            if c <= self.m/2:
                b_epsilon += '1'
            else:
                b_epsilon += '0'
        return int(b_epsilon, 2)

def oxygen_rating(data):
    i = 0
    zero_data = []
    one_data = []

    while len(data) > 1 and i < len(data[0]):
        for d in data:
            if d[i] == '0':
                zero_data.append(d)
            else:
                one_data.append(d)
        if len(zero_data) > len(one_data):
            data = zero_data
        else:
            data = one_data
        one_data, zero_data = [], []
        i += 1

    return int(data[0], 2)


def co2_rating(data):
    i = 0
    zero_data = []
    one_data = []

    while len(data) > 1 and i < len(data[0]):
        for d in data:
            if d[i] == '0':
                zero_data.append(d)
            else:
                one_data.append(d)
        if len(zero_data) <= len(one_data):
            data = zero_data
        else:
            data = one_data
        one_data, zero_data = [], []
        i += 1

    return int(data[0], 2)


if __name__ == '__main__':
    bit_counter = BitCounter(12)
    data = []
    with open('input.txt', 'r') as f:
        for l in f:
            data.append(l)
            bit_counter.count(l)
    print(bit_counter.gamma() * bit_counter.epsilon())
    print(oxygen_rating(data))
    print(co2_rating(data))
    print(oxygen_rating(data) * co2_rating(data))
