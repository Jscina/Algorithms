# Big O -> 2^n
def fib(n: int, memo: dict | None = None) -> int:
    """Returns the n-th number in the Fibonacci sequence."""
    if memo is None:
        memo = dict()
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
        return n
    f = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = f
    return f


def main():
    res = [fib(i) for i in range(100)]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
