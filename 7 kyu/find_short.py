def find_short(s):
    return len(sorted(s.split(), key=len)[0])


print(find_short("bitcoin take over the world maybe who knows perhaps"))