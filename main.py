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

    items_less, pivot_items, items_greater = [], [], []

    for item in list_items:
        if item < pivot:
            items_less.append(item)
        elif item == pivot:
            pivot_items.append(item)
        else:
            items_greater.append(item)

    return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
    )


def get_random_numbers(length: int = 15, minimum: int = 1,
                       maximum: int = 100) -> list[int]:
    return [random.randint(minimum, maximum) for _ in range(length)]


def main() -> NoReturn:
    countdown(5)
    print(factorial(4))

    print(flatten(names))
    print(palindrome("oso"))
    print(quicksort(get_random_numbers()))
    print(statistics.median([15, 10, 20]))


if __name__ == "__main__":
    main()
