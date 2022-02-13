def longest_consec(strarr, k):
    if k <= 0:
        return ""
    ans = ""
    for i in range(len(strarr)-k+1):
        s = "".join(s for s in strarr[i:i+k])
        if len(s) > len(ans):
            ans = s
    return ans


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
