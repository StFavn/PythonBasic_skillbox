import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def increase(self, multiplier):
        self.r *= multiplier

    def is_intersection(self, oth_crl):
        length_sq = (self.y - oth_crl.y) ** 2 + (self.x - oth_crl.x) ** 2
        if ((self.r + oth_crl.r) ** 2 >= length_sq) and ((self.r - oth_crl.r) ** 2 <= length_sq):
            return True
        return False
