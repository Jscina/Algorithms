import random


def merge(A, p, q, r):
    T = [0] * (r - p + 1)  # Temp array
    n = q
    i = 0
    k = p
    q += 1
    # Merging the two sub-arrays
    while p <= n and q <= r:
        if A[p] <= A[q]:
            T[i] = A[p]
            p += 1
        else:
            T[i] = A[q]
            q += 1
        i += 1

    # Copying the remaining elements
    while p <= n:
        T[i] = A[p]
        p += 1
        i += 1

    # Copying the remaining elements
    while q <= r:
        T[i] = A[q]
        q += 1
        i += 1

    # Copying the sorted elements to the original array
    for i in range(len(T)):
        A[k + i] = T[i]


def merge_sort(A: list[int], p: int, r: int):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def main() -> None:
    test = [random.randint(0, 100) for _ in range(10)]
    # It modified the test array, so we need to copy it to see the changes
    test_copy = test.copy()
    merge_sort(test_copy, 0, len(test) - 1)
    print(f"Before sorting: {test}", f"After sorting:{test_copy}", sep="\n")


if __name__ == "__main__":
    main()
