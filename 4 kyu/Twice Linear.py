def dbl_linear_fast(n):
    u = 1
    y_queue = []
    z_queue = []

    for _ in range(n):
        y_queue.append(2*u+1)
        z_queue.append(3*u+1)
        u = min(y_queue[0], z_queue[0])
        if u == y_queue[0]: y_queue.pop(0)
        if u == z_queue[0]: z_queue.pop(0)

    return u


print(dbl_linear_fast(60000))