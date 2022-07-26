class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)
# Adding two fraction number

    def __add__(self, other):
        tempd = self.den*other.den
        tempn = (other.den*self.num)+(self.den*other.num)
        return "{}/{}".format(tempn, tempd)
# Subtracting two fraction number

    def __sub__(self, other):
        tempd = self.den*other.den
        tempn = (other.den*self.num)-(self.den*other.num)
        return "{}/{}".format(tempn, tempd)
# Multiplication two fraction number

    def __mul__(self, other):
        tempn = self.num*other.num
        tempd = self.den*other.den
        return "{}/{}".format(tempn, tempd)
# Dividing two fraction number

    def __truediv__(self, other):
        tempn = self.num*other.den
        tempd = self.den*other.num
        return "{}/{}".format(tempn, tempd)


y = Fraction(3, 4)
x = Fraction(4, 3)
print(x+y)
print(y-x)
print(x*y)
print(x/y)
