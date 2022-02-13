import unittest
import re
from math import comb


def binomial(a, b, n, i):
    return comb(n, i)*pow(a, i)*pow(b, n-i)


def expand(expr):
    a, x, b, n = re.findall(r"\((-*\d*)(\D)([+-]\d*)\D*(\d+)", expr)[0]
    a, b, n = int(a+"1") if a in ["", "-"] else int(a), int(b), int(n)
    result = ""
    for i in range(n, -1, -1):
        coefficient = binomial(a, b, n, i)
        if coefficient < 0: result += "-"
        elif i != n: result += "+"
        if abs(coefficient) != 1 or i == 0: result += str(abs(coefficient))
        if i > 1: result += f"{x}^{i}"
        elif i > 0: result += x
    return result



# Tests

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(expand("(x+1)^0"), "1")

    def test_2(self):
        self.assertEqual(expand("(x+1)^1"), "x+1")

    def test_3(self):
        self.assertEqual(expand("(x+1)^2"), "x^2+2x+1")

    def test_4(self):
        self.assertEqual(expand("(x-1)^0"), "1")

    def test_5(self):
        self.assertEqual(expand("(x-1)^1"), "x-1")

    def test_6(self):
        self.assertEqual(expand("(x-1)^2"), "x^2-2x+1")

    def test_7(self):
        self.assertEqual(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")

    def test_8(self):
        self.assertEqual(expand("(-x-4)^1"), "-x-4")


if __name__ == "__main__":
    unittest.main()