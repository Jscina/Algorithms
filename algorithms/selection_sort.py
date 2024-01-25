# O(n^2) time | O(1) space
def SelectionSort(A: list[int]):
    for i in range(len(A)):
        min_ = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_]:
                min_ = j
        A[i], A[min_] = A[min_], A[i]


def main():
    import random

    test = [random.randint(0, 100) for _ in range(100)]
    SelectionSort(test)


if __name__ == "__main__":
    main()
