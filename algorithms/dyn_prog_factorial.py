F = [-1]


def factorial(n: int) -> int:
    global F

    # Extend F to ensure it has capacity to store up to n!
    size = n + 1
    cur_size = len(F)
    if size > cur_size:
        F.extend([-1] * (size - cur_size))

    # Base Case 0! and 1! == 1
    if F[0] != 1 and F[1] != 1:
        F[0] = F[1] = 1

    # Return previously calculated value n if available
    if F[n] != -1:
        return F[n]

    # Start from 1 because 0! = 1! = 1
    last_calculated = 1
    for i in range(2, n + 1):
        # Calculate the last known value up to n
        if F[i] == -1:
            F[i] = F[i - 1] * i
        last_calculated = i

    return F[last_calculated]


def main() -> None:
    tests = [3, 4, 6, 34, 100]
    for n in tests:
        print(F)
        print(factorial(n))


if __name__ == "__main__":
    main()
