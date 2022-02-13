def pascal(p):
    tri = [[1], [1, 1]]
    if p == 1: return tri[:1]
    elif p == 2: return tri
    else:
        for i in range(2, p):
            tri.append([1]+[tri[-1][k] + tri[-1][k+1] for k in range(i-1)]+[1])
    return tri
