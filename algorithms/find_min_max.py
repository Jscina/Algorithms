def min_max(arr: list[int]) -> str:
    min, max = arr[0], arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return f"Min: {min}, Max: {max}"


def main() -> None:
    import random

    tests = [random.randint(0, 100) for _ in range(10)]
    print(*tests, sep=", ")
    res = min_max(tests)
    print(res)


if __name__ == "__main__":
    main()
