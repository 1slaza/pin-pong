class Donkey():
    def __init__(self, name, cargo, age):
        self.name = name
        self.cargo = cargo
        self.age = age
    def info(self):
        print("donkey-boy" , self.name, ",", self.cargo)

    def cry(self):
        return "я_не_негр " * self.age

    def work_hard(self, amount):
        if amount > 0:
            a = amount // 5
            self.age = self.age - a

        else:
            self.age + 2



    def carry(self, load):
        if load >= self.cargo:
            return True
        else:
            return False


#hi

d = Donkey('Pinoccio', 10, 5)
d.info()
print(d.cry())
d.work_hard(16)
print(d.cry())
print(d.carry(10))






