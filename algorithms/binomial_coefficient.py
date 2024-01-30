def binomial_coef(n: int, k: int) -> int:
    def factorial(j: int) -> int:
        s = 1
        for i in range(1, j + 1):
            s *= i
        return s

    return factorial(n) // factorial(k) * factorial(n - k)


def binomial_coef_opt(n: int, k: int) -> int:
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    def min(a: int, b: int) -> int:
        return a if a < b else b

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


def main():
    print(binomial_coef_opt(5, 2))


if __name__ == "__main__":
    main()
