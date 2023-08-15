


def delivery(counter = 0) -> None:
    if counter == 10:
        print("santa termino de recorrer las casas")
        return

    print(f"Deliver to house {counter+1}")
    delivery(counter+1)



def main() -> None:
    delivery()

if  __name__ == "__main__":
    main()