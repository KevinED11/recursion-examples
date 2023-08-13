import statistics
from typing import NoReturn
from itertools import chain
import random


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
    length_list_items = len(list_items)

    if length_list_items <= 1:
        return list_items

    pivot = statistics.median(
        [
            list_items[0],
            list_items[length_list_items // 2],
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


def get_random_numbers(length=15, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))

    return numbers


def main() -> NoReturn:
    countdown(5)
    print(factorial(4))

    print(flatten(names))
    print(palindrome("oso"))
    print(quicksort(get_random_numbers()))


if __name__ == "__main__":
    main()
