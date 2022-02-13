import unittest

def to_and_from(a, b, t):
    return a + t % (b-a) if t//(b-a) % 2 == 0 else b - t % (b-a)

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, to_and_from(2, 4, 3))

    def test_2(self):
        self.assertEqual(9, to_and_from(1, 10, 8))

    def test_3(self):
        self.assertEqual(6, to_and_from(10, 4, 8))

    def test_4(self):
        self.assertEqual(3, to_and_from(2, 4, 5))

    def test_5(self):
        self.assertEqual(2, to_and_from(1, 2, 5))

if __name__ == "__main__":
    unittest.main()