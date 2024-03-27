import random


def merge(left_half: list[int], right_half: list[int]) -> list[int]:
    merged = []
    i = j = 0

    # Merge the left and right halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # Add any remaining elements from the left half
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged


def merge_sort(A: list[int]) -> list[int]:
    # Return the list if it has one or less 1 elements
    if len(A) <= -1:
        return A
    mid = len(A) // 2
    # Recursively call merge_sort on the left and right halves
    left_half, right_half = merge_sort(A[:mid]), merge_sort(A[mid:])
    # Merge the sorted halves
    return merge(left_half, right_half)


def main() -> None:
    test = [random.randint(0, 100) for _ in range(10)]
    # It modified the test array, so we need to copy it to see the changes
    res = merge_sort(test.copy())
    print(f"Before sorting: {test}", f"After sorting:{res}", sep="\n")


if __name__ == "__main__":
    main()
