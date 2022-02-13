def permutations(string):
    perms = set()
    for i in range(len(string)):
        if len(string) == 1:
            return {string}
        for perm in permutations(string[:i]+string[i+1:]):
            perms.add(string[i]+perm)
    return list(perms)


print(permutations("cat"))
