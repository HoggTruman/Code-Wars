import unittest
import math as m


def middle_permutation(string):
    string = sorted(string)
    result = ""
    rem = (m.factorial(len(string)) + 1)//2
    for i in range(len(string)-1, -1, -1):
        i_fac = m.factorial(i)
        result += string.pop((rem-1) // i_fac)
        rem %= i_fac
    return result


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_decompose_5(self):
        self.assertEqual("bac", middle_permutation("abc"))


if __name__ == "__main__":
    unittest.main()

