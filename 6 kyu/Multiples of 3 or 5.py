def solution(number):
    sol = 0
    for num in range(1,number):
        if num % 3 == 0 or num % 5 == 0:
            sol += num
    return sol