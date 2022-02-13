import unittest


# find the one group closest to center and remove first???
# need the middle numbered group, the size doesnt matter at all (number of elements within), it is purely whether it is a single or group.

"""
1) find groups
2) remove group closest to center or if there are none, remove central block
3) repeat

"""
# WORKS

# def array_erasing(a):
#     count = 0
#     while a:
#         group_num = 0 # using 0 based group numbering
#         groups = {} # group_num: (start, end)
#         i = 0
#         while i < len(a) - 1:
#             if a[i] == a[i+1]:
#                 l = 1
#                 while i < len(a) - 1 and a[i] == a[i+1]:
#                     i += 1
#                     l += 1
#                 groups[group_num] = (i-l+1, i)
#             group_num += 1
#             i += 1
#
#         med = group_num//2
#         count += 1
#         if groups:
#             to_remove = min(groups, key=lambda x: abs(med-x))
#             start, end = groups[to_remove]
#             a = a[:start] + a[end+1:]
#         else:
#             a = a[:med] + a[med+1:]
#
#     return count


# CLEANUP

def array_erasing(a):
    count = 0
    while a:
        group_num, groups = 0, {}
        i = 0
        while i < len(a) - 1:
            if a[i] == a[i+1]:
                s = i
                while i < len(a) - 1 and a[i] == a[i+1]:
                    i += 1
                groups[group_num] = (s, i)
            group_num += 1
            i += 1

        med = group_num//2
        count += 1

        if groups:
            to_remove = min(groups, key=lambda x: abs(med-x))
            start, end = groups[to_remove]
            a = a[:start] + a[end+1:]
        else:
            a = a[:med] + a[med+1:]
    return count


# Tests
class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(array_erasing([1]), 1)

    def test_2(self):
        self.assertEqual(array_erasing([1, 1, 1]), 1)

    def test_3(self):
        self.assertEqual(array_erasing([0, 1, 1, 1, 0]), 2)


if __name__ == "__main__":
    unittest.main()




