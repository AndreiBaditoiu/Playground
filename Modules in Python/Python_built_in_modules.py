import sys
from random import randint

#
#
# my_list = [1,2,3,4,5]
# random.shuffle(my_list)
# print(my_list)

# print(sys)
# print(type(sys))

# guess a number game
# n = randint(1, 100)
# guess = 0
# while guess != n:
#     guess = int(input('Enter a number between 1 and 100: '))
#     if guess < n:
#         print('Too low')
#     elif guess > n:
#         print('Too high')
#     else:
#         print('You are a genius')

# for IDE
answer = randint(1, 10)

while True:
    try:

        guess = int(input("Guess a number between 1 ~ 10: "))

        if 0 < guess < 11:
            if guess == answer:
                print("You are a genius!")
                break
        else:
            print("Hey! Bozo, I said 1~10!")
    except ValueError:
        print("Please enter a number")
        continue

# for terminal
# answer = randint(int(sys.argv[1]), int(sys.argv[10]))
#
# while True:
#     try:
#
#         guess = int(input("Guess a number between 1 ~ 10: "))
#
#         if 0 < guess < 11:
#             if guess == answer:
#                 print("You are a genius!")
#                 break
#         else:
#             print("Hey! Bozo, I said 1~10!")
#     except ValueError:
#         print("Please enter a number")
#         continue


