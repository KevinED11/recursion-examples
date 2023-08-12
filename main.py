from typing import NoReturn


def countdown(n: int) -> NoReturn:
    print(n)
    if n > 0:
        countdown(n - 1)


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


def main() -> NoReturn:
    countdown(5)
    print(factorial(4))


if __name__ == "__main__":
    main()
