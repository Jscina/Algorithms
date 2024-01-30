# Big O -> 2^n
def fib(n: int, memo: dict = dict()) -> int:
    """Returns the n-th number in the Fibonacci sequence."""
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
        return n
    f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return f


def main():
    for i in range(100):
        print(fib(i))


if __name__ == "__main__":
    main()
