import unittest
import re


def domain_name(url):
    return re.findall(r"^(?:https://|http://)?(?:www\.)?([^.]*)", url)[0]


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual("google", domain_name("www.google.com"))


if __name__ == "__main__":
    unittest.main()