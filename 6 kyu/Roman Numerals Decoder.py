def solution(roman):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman)):
        if i == len(roman) - 1 or d[roman[i]] >= d[roman[i+1]]:
            result += d[roman[i]]
        else:
            result -= d[roman[i]]
    return result


