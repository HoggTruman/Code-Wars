import unittest


def bonus(arr, s):
    k = round(s/sum(1/x for x in arr))
    return [round(k/d) for d in arr]


class Tests(unittest.TestCase):
    def test_1(self):
        expected = [1860, 13640, 2728]
        obtained = bonus([22, 3, 15], 18228)
        self.assertEqual(expected, obtained)


if __name__ == "__main__":
    unittest.main()