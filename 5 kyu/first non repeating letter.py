def first_non_repeating_letter(word):
    seen = {}
    for c in word.lower():
        if c in seen:
            seen[c] = 1
        else:
            seen[c] = 0

    for c in word:
        if seen[c.lower()] == 0:
            return c
    return ""


print(first_non_repeating_letter("aabcbdeeeef"))
