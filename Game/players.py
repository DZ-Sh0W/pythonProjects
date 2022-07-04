class Players:
    def __init__(self, name, hp, atk, p_damage):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.p_damage = p_damage

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.atk

    def get_damage(self):
        return self.p_damage
