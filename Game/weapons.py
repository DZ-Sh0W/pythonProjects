class Weapons:
    def __init__(self, w_name, w_atk):
        self.w_name = w_name
        self.w_atk = w_atk

    def get_weapon_name(self):
        return self.w_name

    def get_weapon_attack(self):
        return self.w_atk
