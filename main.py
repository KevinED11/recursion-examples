import statistics
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


def quicksort(list_items: list) -> list:
    if len(list_items) <= 1:
        return list_items

    pivot = statistics.median(
        [
            list_items[0],
            list_items[len(list_items) // 2],
            list_items[-1]
        ]
    )

    items_less, pivot_items, items_greater = (
        [n for n in list_items if n < pivot],
        [n for n in list_items if n == pivot],
        [n for n in list_items if n > pivot],
    )

    return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
    )


def main() -> NoReturn:
    countdown(5)
    print(factorial(4))

    print(flatten(names))
    print(palindrome("oso"))
    print(quicksort([1, 45, 5, 25, 9, 30, 9, 10]))


if __name__ == "__main__":
    main()
