from players import *

n = int(input("How many players you want to add : "))
for i in range(n):
    i += 1
    print("Hello player", i)
    name = input("Enter your name : ")
    player = Players(name, Players.hp, Players.atk, Players.damage)
    print(" Name :", name, "\n", "HP :", player.get_hp(), "\n", "Attack :", player.get_attack())
    print()
