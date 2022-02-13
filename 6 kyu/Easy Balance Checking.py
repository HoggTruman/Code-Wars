import unittest
import re

#Line separator is \r\n in Python
def balance(book):
    book = re.sub(r"[^0-9a-zA-Z.\n ]", "", book)
    lines = book.split('\n')
    og = float(lines.pop(0))
    spent, count = 0, 0
    sol = f"Original Balance: {og:.2f}\r\n"
    for line in lines:
        if line:
            num, cat, cost = line.split()
            spent += float(cost)
            sol += f"{num} {cat} {float(cost):.2f} Balance {og - spent:.2f}\r\n"
            count += 1
    return sol + f"Total expense  {spent:.2f}\r\nAverage expense  {spent/count:.2f}"



class Tests(unittest.TestCase):
    def test_1(self):
        book = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""
        b1sol = b1sol = """Original Balance: 1000.00\r
125 Market 125.45 Balance 874.55\r
126 Hardware 34.95 Balance 839.60\r
127 Video 7.45 Balance 832.15\r
128 Book 14.32 Balance 817.83\r
129 Gasoline 16.10 Balance 801.73\r
Total expense  198.27\r
Average expense  39.65"""
        self.assertEqual(b1sol, balance(book))

    def test_2(self):
        b2 = """1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""
        b2sol = """Original Balance: 1233.00\r
125 Hardware 24.80 Balance 1208.20\r
123 Flowers 93.50 Balance 1114.70\r
127 Meat 120.90 Balance 993.80\r
120 Picture 34.00 Balance 959.80\r
124 Gasoline 11.00 Balance 948.80\r
123 Photos 71.40 Balance 877.40\r
122 Picture 93.50 Balance 783.90\r
132 Tyres 19.00 Balance 764.90\r
129 Stamps 13.60 Balance 751.30\r
129 Fruits 17.60 Balance 733.70\r
129 Market 128.00 Balance 605.70\r
121 Gasoline 13.60 Balance 592.10\r
Total expense  640.90\r
Average expense  53.41"""
        self.assertEqual(b2sol, balance(b2))


if __name__ == "__main__":
    unittest.main()