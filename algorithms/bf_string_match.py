def bf_str_match(T: str, P: str) -> int:
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        j = 0
        while j < m and P[j] == T[i + j]:
            j += 1
        if i == m:
            return i
    return -1


match = "YOU"
text = "IT IS NEVER LATE TO BE WHAT YOU MIGHT HAVE BEEN"

res = bf_str_match(text, match)
print(res)
