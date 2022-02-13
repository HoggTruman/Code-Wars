import unittest

def look_and_say(data, maxlen):
    result, prev = [], data
    while len(result) < maxlen:
        layer, run_start = "", 0
        for i in range(len(prev)):
            if prev[i] != prev[run_start]:
                layer += str(i-run_start) + prev[run_start]
                run_start = i
        result.append(layer+str(len(prev)-run_start)+prev[-1])
        prev = result[-1]
    return result


class Tests(unittest.TestCase):
    def test_1(self):
        expected = ['11', '21', '1211', '111221', '312211', '13112221', '1113213211', '31131211131221', '13211311123113112211', '11131221133112132113212221']
        obtained = look_and_say('1', 10)
        self.assertEqual(expected, obtained)

    def test_2(self):
        expected = ['111312', '31131112', '1321133112', '11131221232112', '31131122111213122112', '13211321223112111311222112', '1113122113121122132112311321322112', '311311222113111221221113122112132113121113222112']
        obtained = look_and_say('132', 8)
        self.assertEqual(expected, obtained)

if __name__ == "__main__":
    unittest.main()
