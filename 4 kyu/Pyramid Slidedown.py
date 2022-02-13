def longest_slide_down(pyramid):
    for i in range(1, len(pyramid)):
        pyramid[i][0] += pyramid[i-1][0]
        pyramid[i][-1] += pyramid[i-1][-1]
        if i > 1:
            for j in range(1, len(pyramid[i])-1):
                pyramid[i][j] += max(pyramid[i-1][j-1], pyramid[i-1][j])

    return max(pyramid[-1])


print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))

