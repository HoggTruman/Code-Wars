import unittest
import math as m


# 1 degree = 60 minutes (60'), 1 minute = 60 seconds (60'')

def solve(a, b, c, alpha, beta, gamma):
    alpha, beta, gamma = m.radians(alpha), m.radians(beta), m.radians(gamma)
    x = m.cos(alpha)*a - m.sin(beta)*b - m.cos(gamma)*c
    y = m.sin(alpha)*a + m.cos(beta)*b - m.sin(gamma)*c
    tOC = m.degrees(m.atan(abs(y/x)) if x >= 0 else m.pi - m.atan(abs(y/x)))

    return [round((x**2+y**2)**0.5),
            int(tOC),
            int((tOC - int(tOC))*60),
            int((tOC * 3600) % 60)]


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual([15, 135, 49, 18], solve(12, 20, 18, 45, 30, 60))
