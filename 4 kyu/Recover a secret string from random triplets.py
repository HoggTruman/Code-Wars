import unittest

def recoverSecret(triplets):
    result = ""
    i = -1
    while triplets:
        i = (i + 1) % len(triplets)
        if all(triplets[i][-1] not in triplets[j][:-1] for j in range(len(triplets))):
            to_add = triplets[i][-1]
            if all(triplets[i] == triplets[z] for z in range(len(triplets))):
                for t in reversed(triplets[i]):
                    result = t + result
            else:
                result = to_add + result
            l, k = len(triplets), 0
            while k < l:
                if triplets[k][-1] == to_add:
                    if len(triplets[k]) == 3:
                        triplets[k].pop()
                        k += 1
                    else:
                        triplets.pop(k)
                        l -= 1
                else:
                    k += 1
    return result



class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_whatisup(self):
        secret = "whatisup"
        triplets = [
            ['t', 'u', 'p'],
            ['w', 'h', 'i'],
            ['t', 's', 'u'],
            ['a', 't', 's'],
            ['h', 'a', 'p'],
            ['t', 'i', 's'],
            ['w', 'h', 's']
        ]
        self.assertEqual(secret, recoverSecret(triplets))



if __name__ == "__main__":
    unittest.main()


