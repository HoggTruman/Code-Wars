import unittest
import numpy as np

def spiralize(size):
    spiral = np.array([[0]*size for _ in range(size)])
    i, j = 0, 0
    while True:
        while j in [size-1, size-2] or spiral[i][j+1] == 0:
            spiral[i][j] = 1
            if j != size-2 and (j == size-1 or spiral[i][j+2] == 1):
                break
            j += 1
        # exit condition
        if spiral[i+2][j] == 1 or spiral[i+1][j-1]:
            while spiral[1][0] == 1:
                spiral = np.rot90(spiral)
            return spiral.tolist()

        i, j = size - j - 1, 0 if j == size-1 else i
        spiral = np.rot90(spiral)


class Tests(unittest.TestCase):
    def test_5(self):
        self.assertEqual(spiralize(5), [[1, 1, 1, 1, 1],
                                          [0, 0, 0, 0, 1],
                                          [1, 1, 1, 0, 1],
                                          [1, 0, 0, 0, 1],
                                          [1, 1, 1, 1, 1]])
    def test_4(self):
        self.assertEqual(spiralize(4), [[1, 1, 1, 1],
                                        [0, 0, 0, 1],
                                        [1, 0, 0, 1],
                                        [1, 1, 1, 1]])
    def test_8(self):
        self.assertEqual(spiralize(8), [[1, 1, 1, 1, 1, 1, 1, 1],
                                        [0, 0, 0, 0, 0, 0, 0, 1],
                                        [1, 1, 1, 1, 1, 1, 0, 1],
                                        [1, 0, 0, 0, 0, 1, 0, 1],
                                        [1, 0, 1, 0, 0, 1, 0, 1],
                                        [1, 0, 1, 1, 1, 1, 0, 1],
                                        [1, 0, 0, 0, 0, 0, 0, 1],
                                        [1, 1, 1, 1, 1, 1, 1, 1]])


if __name__ == "__main__":
    unittest.main()