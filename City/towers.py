class Batiment:
    def __init__(self, name, address, etages):
        self.name = name
        self.address = address
        self.etages = etages

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_etages(self):
        return self.etages


class Immeuble(Batiment):
    def __init__(self, name, address, etages, balcons):
        super(Immeuble, self).__init__(name, address, etages)
        self.balcons = balcons

    def get_balcons(self):
        return self.balcons


class Supermarket(Batiment):
    def __init__(self, name, address, etages, rayons):
        super(Supermarket, self).__init__(name, address, etages)
        self.rayons = rayons

    def get_rayons(self):
        return self.rayons


class Bank(Batiment):
    def __init__(self, name, address, etages, coffres):
        super(Bank, self).__init__(name, address, etages)
        self.coffres = coffres

    def get_coffres(self):
        return self.coffres


print("Towers available : ", "\n", "1/ Immeuble.", "\n", "2/ Supermarket.", "\n", "3/ Bank.")
tower = input("Choose a tower to construct : ")
if tower in ["1", "Immeuble"]:
    num = int(input("How many : "))
    print()
    for i in range(num):
        i += 1
        build = Immeuble(input("Name : "), input("Address : "), int(input("Etages : ")), int(input("Balcons : ")))
        print()
        print("Immeuble", i, "\n", "Name :", build.get_name(), "\n", "Address :", build.get_address(), "\n",
              "Etages :", build.get_etages(), "\n", "Balcons :", build.get_balcons())
        print()
elif tower in ["2", "Supermarket"]:
    num = int(input("How many : "))
    print()
    for i in range(num):
        i += 1
        build = Supermarket(input("Name : "), input("Address : "), int(input("Etages : ")), int(input("Rayons : ")))
        print()
        print("Supermarket", i, "\n", "Name :", build.get_name(), "\n", "Address :", build.get_address(), "\n",
              "Etages :", build.get_etages(), "\n", "Rayons :", build.get_rayons())
        print()
elif tower in ["3", "Bank"]:
    num = int(input("How many : "))
    print()
    for i in range(num):
        i += 1
        build = Bank(input("Name : "), input("Address : "), int(input("Etages : ")), int(input("Coffres : ")))
        print()
        print("Bank", i, "\n", "Name :", build.get_name(), "\n", "Address :", build.get_address(), "\n",
              "Etages :", build.get_etages(), "\n", "Coffres :", build.get_coffres())
        print()
