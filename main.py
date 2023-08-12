from typing import NoReturn


def countdown(n: int) -> NoReturn:
    print(n)
    if n > 0:
        countdown(n - 1)


def main() -> NoReturn:
    countdown(5)


if __name__ == "__main__":
    main()
