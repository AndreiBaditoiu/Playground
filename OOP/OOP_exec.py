# class Cat:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 1 Instantiate the Cat object with 3 cats
#
#
# cat1 = Cat('Mary', 20)
# cat2 = Cat('Tom', 30)
# cat3 = Cat('Harry', 40)
# print(cat1.name, cat1.age)
# print(cat2.name, cat2.age)
# print(cat3.name, cat3.age)
#
#
# # 2 Create a function that finds the oldest cat
# def oldest_cat(*cats):
#     return max(cats, key=lambda cat: cat.age)
#
#
# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# oldest = oldest_cat(cat1, cat2, cat3)
# print(f'Oldest cat is {oldest.name} and is {oldest.age} years old')


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership is True:
            self.name = name  # attributes or proprieties
            self.age = age

    def run(self):
        return self

    def speak(self):
        print( f"I am {self.name} and {self.age} years old")


player1 = PlayerCharacter('Tom', 25)
player1.speak()