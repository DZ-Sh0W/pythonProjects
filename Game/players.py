class Players:
    def __init__(self, name, hp, atk, damage):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.damage = damage

    hp = 100
    atk = 10
    damage = hp - atk

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.atk

    def get_damage(self):
        return self.damage
