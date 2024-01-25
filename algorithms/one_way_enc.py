input = 151498928


def encrypt(value: int) -> int:
    return (value * 123456789) & (value + 123456789)


def decrypt() -> None:
    for i in range(999999999):
        output = (i * 123456789) & (i + 123456789)
        if output == input:
            print(i)


def main():
    decrypt()


if __name__ == "__main__":
    main()
