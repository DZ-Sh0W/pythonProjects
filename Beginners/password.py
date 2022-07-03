def main():
    from random import shuffle
    from random import choice

    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "%@-_!.#"

    characters = list(letters + capital_letters + numbers + symbols)

    #print(characters)
    #print("".join(characters))

    shuffle(characters)

    #print(characters)
    #print("".join(characters))

    length = int(input("Choose password length : "))

    password = []
    for i in range(length):
        password.append(choice(characters))
        #print(password)

    print()
    print("".join(password))

while True:
    print()
    main()

