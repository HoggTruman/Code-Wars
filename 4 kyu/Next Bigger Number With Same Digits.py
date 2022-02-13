import unittest

def next_bigger(n):
    n = [d for d in str(n)]
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            k = i
            for j in range(i, len(n)):
                if n[i-1] < n[j] < n[k]:
                    k = j
            n[i-1], n[k] = n[k], n[i-1]
            n[i:] = sorted(n[i:])
            return int("".join(n))
    return -1


# tests (just use unittest in the future)
tests = [12, 513, 2017, 414, 144, 1234567890, 388753]
expected = [21, 531, 2071, 441, 414, 1234567908, 533788]

for i in range(len(tests)):
    obtained = next_bigger(tests[i])
    if obtained == expected[i]:
        print("OK!")
    else:
        print(f"TEST FAILED ({tests[i]}), EXPECTED:{expected[i]}, OBTAINED:{obtained}")
