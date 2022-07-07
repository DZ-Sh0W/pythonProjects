from players import *
from weapons import *

player = Players((input("Name : ").split(", ")), int(input("HP : ")), int(input("Attack : ")), 0)
print()
liste = list(player.name)
leng = len(liste)

for i in range(leng):
    i += 0
    print(liste[i], "is player", i+1, "!")
    print(" Name :", liste[i], "\n", "HP :", player.get_hp(), "\n", "Attack :", player.get_attack())
    print()

print(liste[0], "attack first.")
print()

print("your available weapons")

wp0 = [input("0) enter a weapon"), int(input("enter attack :"))]
wp1 = [input("1) enter a weapon"), int(input("enter attack :"))]
wp2 = [input("2) enter a weapon"), int(input("enter attack :"))]
wp3 = [input("3) enter a weapon"), int(input("enter attack :"))]

weapon0 = Weapons(wp0[0], wp0[1])
weapon1 = Weapons(wp1[0], wp1[1])
weapon2 = Weapons(wp2[0], wp2[1])
weapon3 = Weapons(wp3[0], wp3[1])

weapons = [weapon0, weapon1, weapon2, weapon3]

choose = int(input("Player to attack : "))

if 0 <= choose-1 < leng:
    choice = int(input("Choose your weapon from 0 to 3: "))
    if 0 <= choice < 4:
        Players.p_damage = player.hp - weapons[choice].get_weapon_attack()
        print("You have damaged", player.get_name()[choose-1], "by", weapons[choice].get_weapon_name(), "with", weapons[choice].get_weapon_attack(), "points.")
        print("Now, his remain health is", Players.p_damage, "points.")
    else:
        print("Error !")
else:
    print("Unknown !")
