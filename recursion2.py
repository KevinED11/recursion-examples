

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


def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

def main() -> None:
    delivery()
    print(factorial_recursive(5))


if __name__ == "__main__":
        main()
