def find_nb(m):
    n = 0
    while m > 0:
        n += 1
        m -= n**3
    return n if m == 0 else -1

print(find_nb(4183059834009))
print(find_nb(24723578342962))
