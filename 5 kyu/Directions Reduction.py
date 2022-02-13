def dirReduc(arr):
    stack = []
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    for dir in arr:
        if stack and dir == opposite[stack[-1]]:
            stack.pop()
        else:
            stack.append(dir)
    return stack


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
