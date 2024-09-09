# class BigObject:
#     pass
#
#
# obj1 = BigObject()
#
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership is True:
            self.name = name  # attributes or proprieties
            self.age = age

    def run(self):
        return self

    # @staticmethod
    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 44)
print(player1.adding_things(5, 3))
player2 = PlayerCharacter('Tom', 37)
print(player1.name, player1.age)
print(player2.name, player2.age)
player2.attack = 50
print(player1.shout())
print(player2.shout())
print(player2.membership)
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)


# ///// New


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')


# Introspection-the ability to determine the type of object at the runtime
wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100, 'robin@gmail.com')

# wizard1.attack()
# archer1.attack()
print(wizard1.email)
print(archer1.email)
print(dir(wizard1))


# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, User))
# print(isinstance(wizard1, object))

# Polymorphism

def player_attack(char):
    char.attack()

# Multiple inheritance
