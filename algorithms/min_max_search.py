import random


def min_search(A: list[int]) -> int:
    for i in range(len(A)):
        if A[i] < A[0]:
            A[0] = A[i]
    return A[0]


def max_search(A: list[int]) -> int:
    for i in range(len(A)):
        if A[i] > A[0]:
            A[0] = A[i]
    return A[0]


def main():
    test = [random.randint(1, 100) for _ in range(10)]
    print(test)
    print(min_search(test))
    print(max_search(test))


if __name__ == "__main__":
    main()
