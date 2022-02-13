import unittest


def validate_battlefield(battlefield):
    poss = [[], [], [], []]  # first contains possible 1 positions, second 2 positions, third 3 , fourth 4 positions
    points = set()
    for i in range(10):
        for j in range(10):
            if battlefield[i][j] == 1:
                points.add((i, j))
                poss[0].append((i, j))

                # find vertical length
                v = 1
                while v < 4 and i + v < 10:
                    if battlefield[i + v][j] == 1:
                        poss[v].append([(k, j) for k in range(i, i+v+1)])
                    else: break
                    v += 1

                # find horizontal length
                h = 1
                while h < 4 and j + h < 10:
                    if battlefield[i][j + h] == 1:
                        poss[h].append([(i, k) for k in range(j, j+h+1)])
                    else: break
                    h += 1

    # quick false checks
    if len(points) != 20: return False
    if not all(ship_group for ship_group in poss): return False

    # test for possible
    return scan_possible(set(), 3, 1, 0, poss)


def scan_possible(visited, ship_type, ship_num, start, poss):
    for b in range(start, len(poss[ship_type])):
        if ship_type == 3:
            result = scan_possible(set(poss[ship_type][b]), 2, 1, 0, poss)
            if result: return result
        elif all(c not in visited for c in poss[ship_type][b]):
            if ship_type == 0 and ship_num == 4:
                return True
            elif ship_type == 1 and ship_num == 3:
                if scan_possible(visited.union(poss[ship_type][b]), 0, 1, 0, poss): return True
            elif ship_type == 2 and ship_num == 2:
                if scan_possible(visited.union(poss[ship_type][b]), 1, 1, 0, poss): return True
            else:
                if scan_possible(visited.union(poss[ship_type][b]), ship_type, ship_num+1, b+1, poss): return True
    return False


class Tests(unittest.TestCase):
    def test_battlefield(self):
        self.assertEqual(True, validate_battlefield(
            [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))


if __name__ == "__main__":
    unittest.main()
