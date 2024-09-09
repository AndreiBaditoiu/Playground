# Decorators are connected to functions; in Python, decorators are 'first-class citizens'. They act just like variables.
# Functions act like variables and are first-class citizens.
# def hello():
#     print('Hellllooooo')
#
#
# greet = hello()
# del hello
#
# print(greet)


# def salute(func):
#     func()
#
#
# def reply():
#     print('Still here!')
#
#
# a = salute(reply)
#
# print(a)


# /////////////////

# Higher Order Function – HOC (is a function that takes another function as a parameter or returns it.)

# def greet(func):  # here accepts another function as a parameter
#     func()


# def greet2():  # here it returns another function
#     def func():
#         return 5
#
#     return func()

# /////////

# Decorator – they add extra functionality to functions

# Decorator Pattern
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('***********')
        func(*args, **kwargs)
        print('***********')

    return wrapper


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


@my_decorator
def bye():
    print("see ya later")


hello('hiii', ':)')
# bye()
