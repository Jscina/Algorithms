def hash(key: str) -> int:
    sum, ln = 0, len(key) - 1
    for i, ch in enumerate(key):
        sum += ord(ch) * (128 ** (ln - i))
    return sum


def main():
    test = "sam"
    print(hash(test))


if __name__ == "__main__":
    main()
