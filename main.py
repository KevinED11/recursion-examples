from typing import NoReturn
from itertools import chain


def countdown(n: int) -> NoReturn:
    print(n)
    if n > 0:
        countdown(n - 1)


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]


def flatten(lista: list) -> list:
    result = []

    for item in lista:
        if isinstance(item, list):
            result += flatten(lista=item)
        else:
            result.append(item)

    return result


# unnecessary recursion
def palindrome(text: str) -> bool:
    return text[::-1] == text


def main() -> NoReturn:
    countdown(5)
    print(factorial(4))

    print(flatten(names))
    print(palindrome("oso"))


if __name__ == "__main__":
    main()
