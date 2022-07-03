def main():
    euros = "€"
    dinars = "DA"
    dollars = "$"

    try:
        currency = input("'Amount' 'Currency' : ").split(" ")

        euro_dinar = (float(currency[0])) * 200
        dinar_euro = (float(currency[0])) / 200
        dollar_dinar = (float(currency[0])) * 160
        dinar_dollar = (float(currency[0])) / 160
        euro_dollar = (float(currency[0])) * 1.5
        dollar_euro = (float(currency[0])) / 1.5

        unit = str(input("Choose currency to convert for : "))
        if str(currency[1]) == dinars:
            if unit == euros:
                print(dinar_euro, euros)
            elif unit == dollars:
                print(dinar_dollar, dollars)
        elif str(currency[1]) == euros:
            if unit == dinars:
                print(euro_dinar, dinars)
            elif unit == dollars:
                print(euro_dollar, dollars)
        elif str(currency[1]) == dollars:
            if unit == euros:
                print(dollar_euro, euros)
            elif unit == dinars:
                print(dollar_dinar, dollars)
    except ValueError:
        print("Error !")


main()

while True:
    print()
    main()
