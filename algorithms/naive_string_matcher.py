def naive_string_matcher(T: str, P: str) -> None:
    # T: text, P: pattern
    n, m = len(T), len(P)
    # For each shift s
    for s in range(n - m):
        # If the substring matches the pattern, print the shift
        if T[s : s + m] == P:
            print(f"Pattern occurs with shift {s}")


def main():
    T, P = "there is a theory that the theater is there", "the"
    # O((n-m+1)*m)
    # For each shift we check m characters
    # then we have n-m+1 shifts
    # So the time complexity is O((n-m+1)*m)
    naive_string_matcher(T, P)


if __name__ == "__main__":
    main()
