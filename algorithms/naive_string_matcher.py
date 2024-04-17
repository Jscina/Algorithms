def naive_string_matcher(T: str, P: str) -> None:
    n, m = len(T), len(P)
    for s in range(n - m):
        if T[s : s + m].lower() == P.lower():
            print(f"Pattern occurs with shift {s}")


def main():
    T, P = "There is a theory that the Theater is ThEre", "the"
    naive_string_matcher(T, P)


if __name__ == "__main__":
    main()
