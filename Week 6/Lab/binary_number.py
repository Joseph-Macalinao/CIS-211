class BinaryNumber:
    def __init__(self, bits):
        self.bits = bits

    def __or__(self, other):
        bit_str = []
        for i in range(self.bits):
            if self.bits[i] == 0 or other.bits[i] == 0:
                bit_str.append(1)
            else:
                bit_str.append(0)
        return BinaryNumber(bit_str)

    def __and__(self, other):
        bit_str = []
        for i in range(self.bits):
            if self.bits[i] == 1 and other.bits[i] == 1:
                bit_str.append(1)
            else:
                bit_str.append(0)
        return BinaryNumber(bit_str)

    def left_shift(self):
        self.bits = self.number[1:] + [0]


    def right_shift(self):
        self.bits = [0] + self.bits[:-1]

    def extract(self, start: int, end: int):
        return BinaryNumber(self.bits[start, end])

