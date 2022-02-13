def snail(snail_map):
    result = []
    prev = 0
    while snail_map:
        if prev == 0: # top
            result.extend(snail_map.pop(0))
        elif prev == 1: # right side
            for row in snail_map:
                result.append(row.pop(-1))
        elif prev == 2: # bottom
            result.extend(reversed(snail_map.pop(-1)))
        elif prev == 3:
            for row in reversed(snail_map):
                result.append(row.pop(0))
        prev = (prev + 1) % 4
    return result



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
#array = [[1]]
print(snail(array))