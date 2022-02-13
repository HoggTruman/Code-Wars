def solution(string, markers):
    string_list = string.split("\n")
    for i in range(len(string_list)):
        s = string_list[i]
        for j in range(len(s)):
            if s[j] in markers:
                string_list[i] = s[:j].rstrip()
                break
    return "\n".join(string_list)
