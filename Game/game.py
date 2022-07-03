from players import *
from weapons import *

player1 = Players("WaLiD", Players.hp, Players.atk, Players.p_damage)
player2 = Players("Ramzy", Players.hp, Players.atk, Players.p_damage)

print(" Name :", player1.get_name(), "\n", "HP :", player1.get_hp(), "\n", "Attack :", player1.get_attack())
print()
print(" Name :", player2.get_name(), "\n", "HP :", player2.get_hp(), "\n", "Attack :", player2.get_attack())
print()

print(player1.get_name(), "attack", player2.get_name(), "!")
print()

weapon1 = Weapons("AK47", 30)
weapon2 = Weapons("Knife", 20)
weapon3 = Weapons("Shotgun", 90)

print("Choose a weapons from the list below :", "\n", "1/ Punch", "\n", "2/ AK47", "\n", "3/ Knife", "\n", "4/ Shotgun")
print()

choose = input("Your weapon : ")
if choose in ["1", "Punch"]:
    Players.p_damage = Players.hp - Players.atk
    print("You have damaged", player2.get_name(), "by punch, with", Players.atk, "points.")
    print("Now, his remain health is", Players.p_damage, "points.")
elif choose in ["2", "AK47"]:
    Players.p_damage = Players.hp - weapon1.get_weapon_attack()
    print("You have damaged", player2.get_name(), "by AK47, with", weapon1.get_weapon_attack(), "points.")
    print("Now, his remain health is", Players.p_damage, "points.")
elif choose in ["3", "Knife"]:
    Players.p_damage = Players.hp - weapon2.get_weapon_attack()
    print("You have damaged", player2.get_name(), "by Knife, with", weapon2.get_weapon_attack(), "points.")
    print("Now, his remain health is", Players.p_damage, "points.")
elif choose in ["4", "Shotgun"]:
    Players.p_damage = Players.hp - weapon3.get_weapon_attack()
    print("You have damaged", player2.get_name(), "by Shotgun, with", weapon3.get_weapon_attack(), "points.")
    print("Now, his remain health is", Players.p_damage, "points.")
else:
    print("Error !")
