class User():
    def sign_in(self):
        print('logged in')
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power} and name is {self.name}')
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name} attacking with arrows : arroes left-{self.num_arrows}')
wizard1 = Wizard('jj', 50)
archer1 = Archer('edde', 100)
wizard1.attack()
archer1.attack()


print(isinstance(wizard1, Wizard))