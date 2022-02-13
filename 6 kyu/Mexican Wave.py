def wave(s):
    return [s[:i]+s[i].upper()+s[i+1:] for i in range(len(s)) if s[i] != ' ']

print(wave("dog cat"))