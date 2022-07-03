from random import shuffle

words = input("Mot1/Mot2/Mot3/Mot4... : ")
list = words.split("/")
print(list)
shuffle(list)
print(list)
length = len(list)
if length < 10:
    print("Les deux premiers mots :", list[:2])
elif length >= 10:
    print("Les trois derniers mots :", list[-3:])
