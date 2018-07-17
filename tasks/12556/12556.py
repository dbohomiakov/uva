import sys
from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', 'x y')
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP


def parse_vars(line):
    return tuple(map(Decimal, line.strip().split()))


class Triangle:
    def __init__(self, points):
        points = parse_vars(points)
        self.A, self.B, self.C = [Point(*p) for p in zip(points[0::2],
                                                         points[1::2])]
        self.AB = self.calc_side(self.A, self.B)
        self.AC = self.calc_side(self.A, self.C)
        self.BC = self.calc_side(self.B, self.C)
        # Perimeter midpoints
        self.D = self.E = self.F = None

    def calc_side(self, p1, p2):
        return (pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2)).sqrt()

    def calc_perimetr_midpoints(self):
        ratio_AB = self.calc_midpoint_ratio(self.AB, self.AC, self.BC)
        ratio_CA = self.calc_midpoint_ratio(self.AC, self.BC, self.AB)
        ratio_BC = self.calc_midpoint_ratio(self.BC, self.AB, self.AC)
        D = self.calc_midpoint(self.A, self.B, ratio_AB)
        F = self.calc_midpoint(self.C, self.A, ratio_CA)
        E = self.calc_midpoint(self.B, self.C, ratio_BC)
        return Point(*D), Point(*F), Point(*E)

    def calc_midpoint_ratio(self, side1, side2, side3):
        return (side3 + side1 - side2) / (side2 + side1 - side3)

    def calc_midpoint(self, point_1, point_2, ratio):
        x = (point_1.x + ratio * point_2.x) / (1 + ratio)
        y = (point_1.y + ratio * point_2.y) / (1 + ratio)
        return x, y

    def is_intersect(self):
        """
        Check if CD, AE, BF intersect in the one point.
        """
        self.D, self.F, self.E = self.calc_perimetr_midpoints()
        intersect_point_1 = self.intersect_point(self.D, self.C, self.A, self.E)
        intersect_point_2 = self.intersect_point(self.D, self.C, self.B, self.F)

        x1 = intersect_point_1.x.quantize(Decimal('.000001'),
                                                            rounding=ROUND_HALF_UP)
        x2 = intersect_point_2.x.quantize(Decimal('.000001'),
                                                            rounding=ROUND_HALF_UP)
        y1 = intersect_point_1.y.quantize(Decimal('.000001'),
                                                            rounding=ROUND_HALF_UP)
        y2 = intersect_point_2.y.quantize(Decimal('.000001'),
                                                            rounding=ROUND_HALF_UP)

        # TODO: fix decimal places in perimeter midpoint

        if (x1, y1) == (x2, y2):
            return '{:.6f} {:.6f}'.format(x1, y1)
        return 'ERROR'

    def calc_coef_equation(self, p1, p2):
        """
        Calculate coefficients of equation of the line: a*x + b*y + c = 0
        """
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = p1.x * p2.y - p2.x * p1.y
        return a, b, c

    def intersect_point(self, p1, p2, p3, p4):
        """
        Calculate point of intersection of two lines by 4 points.
        Using:  a1*x + b1*y + c1 = 0
                a2*x + b2*y + c2 = 0
        """
        a1, b1, c1 = self.calc_coef_equation(p1, p2)
        a2, b2, c2 = self.calc_coef_equation(p3, p4)

        if not a1:
            y = - c1 / b1
            x = - (b2 * y - c2) / a2
            return Point(x, y)

        if not a2:
            y = - c2 / b2
            x = - (b1 * y - c1) / a1
            return Point(x, y)
        
        if not b1:
            x = - c1 / a1
            y = (- a2 * x - c2) / b2
            return Point(x, y)
        
        if not b2:
            x = - c2 / a2
            y = (- a1 * x - c1) / b1
            return Point(x, y)
        
        x = (c2 * b1 - c1 * b2) / (b2 * a1 - b1 * a2)
        y = (-c2 - a2 * x) / b2
        return Point(x, y)
        

if __name__ == '__main__':
    file = open('sample.in')#sys.stdin

    test_cases = int(file.readline().strip())

    for i in range(1, test_cases + 1):
        print('Case {}: {}'.format(
            i, Triangle(file.readline()).is_intersect()))

