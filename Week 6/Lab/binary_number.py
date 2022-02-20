class BinaryNumber:
    def __init__(self, bits):
        if type(bits) == list:
            self.bits = bits
        elif type(bits) == int:
            self.bits = list(bits)

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

    def __str__(self):
        return f"{self.bits}"

    def left_shift(self, amount):
        self.bits = self.bits[amount:] + [0] * amount


    def right_shift(self, amount):
        self.bits = [0] * amount + self.bits[:-amount]

    def extract(self, start: int, end: int):
        pass



        # return BinaryNumber(self.bits[start, end])

b = BinaryNumber([1, 1, 1, 1, 1])
b.right_shift(2)
print(b)