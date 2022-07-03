def main():
    price = ()
    product_price = 500

    while price != product_price:
        try:
            price = float(input("Enter a price : "))
            if product_price < price:
                print("Less !")
                print()
            elif product_price > price:
                print("Plus !")
                print()
        except ValueError:
            print("Error !")
            print()

    print("Correct !")


main()
