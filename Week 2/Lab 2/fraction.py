class Fraction:
    def __init__(self, num: int, den: int):
        if den <= 0 or num < 0:
            raise AssertionError("Denominator cannot be 0 and Numerator cannot be negative")
        simp = self.gcd(num, den)
        self.num = int(num / simp)
        self.den = int(den / simp)

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __repr__(self):
        return f'Fraction({self.num},{self.den})'

    def __mul__(self, other):
        return Fraction(self.num * other.num,self.den * other.num)

    def __add__(self, other):
        return Fraction((self.num * other.den) + (other.num * self.den), (self.den * other.den))

    def gcd(self, a, b) -> int:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def simplify(self):
        simp = self.gcd(self.num, self.den)
        self.num = int(self.num / simp)
        self.den = int(self.den / simp)


f1 = Fraction(35,56)
print(f1)

