def get_vowels_numbers(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_numbers = 0

    for letter in word:
        if letter in vowels:
            vowels_numbers += 1
    return vowels_numbers


def main():
    word = str(input("Enter a word : "))
    print("Vowels number is :", get_vowels_numbers(word))


main()
