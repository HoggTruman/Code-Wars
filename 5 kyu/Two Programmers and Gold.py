import unittest
import numpy as np

d = {}

def distribution_of(gold):
    if len(gold) == 1:
        return gold[0], 0
    for i in range(len(gold)):
        d[i] = {}
    return tuple(digging(gold, 0, len(gold) - 1))


def digging(gold, start, end):
    if end in d[start]:
        return d[start][end]
    elif end - start == 1:
        d[start][end] = np.array([max(gold[start:end+1]), min(gold[start:end+1])])
    else:
        d[start][end] = max(np.array([gold[start], 0]) + np.flip(digging(gold, start+1, end)),
                            np.array([gold[end], 0]) + np.flip(digging(gold, start, end-1)),
                            key=lambda x: x[0]
                            )
    return d[start][end]


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(distribution_of([4, 7, 2, 9, 5, 2]), (18, 11))

    def test_2(self):
        self.assertEqual(distribution_of([10]), (10, 0))


if __name__ == "__main__":
    unittest.main()

