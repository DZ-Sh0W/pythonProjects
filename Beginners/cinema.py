def main():
    print("Bienvenue dans 'CinéVIP' !")
    print()

    movies = ["1/ GOT", "2/ Venom", "3/ Thor"]
    print("Voici la liste des films disponibles :")
    print(*movies, sep="\n")
    print()

    m = str(input("Que voulez-vous regarder ? : "))
    m1 = "Venom"
    m2 = "GOT"
    m3 = "Thor"

    venom1 = 15
    venom2 = 25

    got1 = 17
    got2 = 27

    pop = 5

    if m == m1:
        wallet = int(input("Votre monnaie : "))

        if wallet > venom1 or wallet > venom2:
            age = int(input("Votre age s'il vous plait : "))

            if 0 < age < 18 and wallet >= venom1:
                print('Vous payez', venom1, '$')
                corn = str(input('Voulez-vous du Popcorn ? (Oui ou Non) : '))
                a = "Oui"
                b = "Non"

                if corn == a and wallet >= (venom1 + pop):
                    print('Vous devez payez', pop, '$', "supplementaires.")
                    sarf1 = wallet - (venom1 + pop)
                    print('La monnaie est :', sarf1, '$')

                elif corn == a and wallet < (venom1 + pop):
                    print("Vous n'avez pas assez d'argent.")

                elif corn == b:
                    sarf1_1 = wallet - venom1
                    print('La monnaie est :', sarf1_1, '$')

                else:
                    print("Choix incorrect !")

            elif age >= 18 and wallet >= venom2:
                print('Vous payez', venom2, '$')
                corn = str(input('Voulez-vous du Popcorn ? (Oui ou Non) : '))
                a = "Oui"
                b = "Non"

                if corn == a and wallet >= (venom2 + pop):
                    print('Vous devez payez', pop, '$', "supplementaires.")
                    sarf2 = wallet - (venom2 + pop)
                    print('La monnaie est :', sarf2, '$')

                elif corn == a and wallet < (venom2 + pop):
                    print("Vous n'avez pas assez d'argent.")

                elif corn == b:
                    sarf2_1 = wallet - venom2
                    print('La monnaie est :', sarf2_1, '$')

                else:
                    print("Choix incorrect !")

        else:
            print("Pas d'argent")

    elif m == m2:
        wallet = int(input("Votre monnaie : "))

        if wallet > got1 or wallet > got2:
            age = int(input("Votre age s'il vous plait : "))

            if 0 < age < 18 and wallet >= got1:
                print('Vous payez', got1, '$')
                corn = str(input('Voulez-vous du Popcorn ? (Oui ou Non) : '))
                a = "Oui"
                b = "Non"

                if corn == a and wallet >= (got1 + pop):
                    print('Vous devez payez', pop, '$', "supplementaires.")
                    sarf3 = wallet - (got1 + pop)
                    print('La monnaie est :', sarf3, '$')

                elif corn == a and wallet < (got1 + pop):
                    print("Vous n'avez pas assez d'argent.")

                elif corn == b:
                    sarf3_1 = wallet - got1
                    print('La monnaie est :', sarf3_1, '$')

                else:
                    print("Choix incorrect !")

            elif age >= 18 and wallet >= got2:
                print('Vous payez', got2, '$')
                corn = str(input('Voulez-vous du Popcorn ? (Oui ou Non) : '))
                a = "Oui"
                b = "Non"

                if corn == a and wallet >= (got2 + pop):
                    print('Vous devez payez', pop, '$', "supplementaires.")
                    sarf4 = wallet - (got2 + pop)
                    print('La monnaie est :', sarf4, '$')

                elif corn == a and wallet < (got2 + pop):
                    print("Vous n'avez pas assez d'argent.")

                elif corn == b:
                    sarf4_1 = wallet - got2
                    print('La monnaie est :', sarf4_1, '$')

                else:
                    print("Choix incorrect !")

        else:
            print("Pas d'argent")

    elif m == m3:
        print("Coming Soon !")

    else:
        print("Non disponible !")

    print("Merci !")
    print()


while True:
    main()
