

def delivery(counter = 0) -> None:
    if counter == 10:
        print("santa termino de recorrer las casas")
        return

    print(f"Deliver to house {counter+1}")
    delivery(counter+1)


def factorial_recursive(n: int) -> int:
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        result = n * factorial_recursive(n-1)
        print(result)

        return result


def sum_recursive(current_number: int, accumulated_sum: int) -> int:
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)


def list_sum_recursive(input_list: list) -> int:
    # Base case
    if not input_list:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


def main() -> None:
    delivery()
    print(factorial_recursive(5))
    print(sum_recursive(0, 0))
    print(list_sum_recursive([1, 2, 3]))


if __name__ == "__main__":
        main()
