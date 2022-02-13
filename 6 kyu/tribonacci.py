def tribonacci(signature, n):
    result = signature[:n]
    for i in range(len(result), n):
        result.append(sum(result[i-3:]))
    return result

