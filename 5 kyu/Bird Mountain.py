import unittest

def peak_height(m):
    # convert to lists of integers and add border to make easier to work with
    for i in range(len(m)):
        m[i] = m[i].replace(' ', '0')
        m[i] = [0] + [-1 if c == '^' else int(c) for c in m[i]] + [0]
    m = [[0]*len(m[0])] + m + [[0]*len(m[0])]

    # solve the problem
    current, next = 0, 1
    while not all(-1 not in l for l in m):
        print(current)
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == -1 and current in [m[i+1][j], m[i-1][j], m[i][j+1], m[i][j-1]]:
                    m[i][j] = next
        current += 1
        next += 1
    return current

class Tests(unittest.TestCase):
    def test_1(self):
        expected = 3
        obtained = peak_height([
          "^^^^^^        ",
          " ^^^^^^^^     ",
          "  ^^^^^^^     ",
          "  ^^^^^       ",
          "  ^^^^^^^^^^^ ",
          "  ^^^^^^      ",
          "  ^^^^        "
        ]   )
        self.assertEqual(expected, obtained)


if __name__ == "__main__":
    unittest.main()