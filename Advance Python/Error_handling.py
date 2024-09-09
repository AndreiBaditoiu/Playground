# age = input("What is your age? ")# it works
# print(age)
#
# age2 = input("What is your age? ")  # it also works even if input is a string (int expected)
# print(age2)


# Error Handling
# while True:
#     try:
#         age3 = int(input("What is your age? "))  # wrap the input in int to make sure it will receive and int
#         10 / age3
#         print(age3)
#     except ValueError:
#         print("Sorry, that's not an integer")
#     except ZeroDivisionError:
#         print("Please enter age higher than zero")
#     else:
#         print("Thank you!")
#         break


# //////////

# def my_sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f"Please enter two numbers! {err}")
#
#
#
# print(my_sum(1, '2'))


# def my_sum(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f"Please enter two numbers! {err}")
#
#
#
# print(my_sum(1, 0))


# /////////
# Raising errors


while True:
    try:
        age3 = int(input("What is your age? "))  # wrap the input in int to make sure it will receive and int
        10 / age3
        print(age3)
    except ValueError:
        print("Sorry, that's not an integer")
        continue
    except ZeroDivisionError:
        print("Please enter age higher than zero")
        break
    else:
        print("Thank you!")
        break
    finally:
        print("Ok, I'm finally done!")
    print("Can you hear me?")
