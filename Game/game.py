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

weapon1 = Weapons("AK47", 30)
weapon2 = Weapons("Knife", 20)
weapon3 = Weapons("Shotgun", 90)

choose = int(input("Player to attack : "))
print()

if 0 <= choose-1 < leng:
    print("Choose a weapon from the list below :", "\n", "1/ Punch", "\n", "2/ AK47", "\n", "3/ Knife", "\n",
          "4/ Shotgun")
    print()
    choice = input("Your weapon : ")
    print()
    if choice in ["1", "Punch"]:
        Players.p_damage = player.hp - player.atk
        print("You have damaged", player.get_name()[choose-1], "by punch, with", player.atk, "points.")
        print("Now, his remain health is", Players.p_damage, "points.")
    elif choice in ["2", "AK47"]:
        Players.p_damage = player.hp - weapon1.get_weapon_attack()
        print("You have damaged", player.get_name()[choose-1], "by AK47, with", weapon1.get_weapon_attack(), "points.")
        print("Now, his remain health is", Players.p_damage, "points.")
    elif choice in ["3", "Knife"]:
        Players.p_damage = player.hp - weapon2.get_weapon_attack()
        print("You have damaged", player.get_name()[choose-1], "by Knife, with", weapon2.get_weapon_attack(), "points.")
        print("Now, his remain health is", Players.p_damage, "points.")
    elif choice in ["4", "Shotgun"]:
        Players.p_damage = player.hp - weapon3.get_weapon_attack()
        print("You have damaged", player.get_name()[choose-1], "by Shotgun, with", weapon3.get_weapon_attack(), "points.")
        print("Now, his remain health is", Players.p_damage, "points.")
    else:
        print("Weapon not found !")
else:
    print("Unknown !")
