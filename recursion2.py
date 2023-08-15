


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
        print(f"Computing factorial of {n} - need to compute {n-1}!")

        return result

def main() -> None:
    delivery()
    print(factorial_recursive(4))

if  __name__ == "__main__":
    main()