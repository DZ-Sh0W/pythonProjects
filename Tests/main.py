print("Player1, Player2, ...")
players = input("Name : ").split(", ")
print()
liste = list(players)
print(liste)
leng = len(liste)
print()

for i in range(leng):
    i += 0
    print(players[i], "is player", i)
    print()

print(players[0], "attack first")

choose = input("Player to attack : ")

if choose in [players[1], "1"]:
    print("Ba333", players[1]) 
    walid hmar
