def duplicate_encode(word):
    seen = {}
    for c in word.lower():
        if c in seen:
            seen[c] = 1
        else:
            seen[c] = 0

    return "".join(")" if seen[c] == 1 else "(" for c in word.lower())

print(duplicate_encode("orangeso"))

