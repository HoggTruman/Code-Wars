import unittest

def decomposer(n, k):
    if k < 0:
        return None
    elif k == 0:
        return []
    else:
        for i in range(min(int(k**0.5), n-1), 0, -1):
            seq = decomposer(i, k-i**2)
            if seq != None:
                return seq + [i]


def decompose(n):
    k = n**2
    return decomposer(n, k)


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_decompose_5(self):
        self.assertEqual([3, 4], decompose(5))


if __name__ == "__main__":
    unittest.main()
