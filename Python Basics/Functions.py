# Functions are very important; they are part of DRY concept.
# parameters (positional arguments)
# def say_hello(name, emoji):
#     print(f'Hello {name} {emoji}')


# arguments
# say_hello('Andrei', ':)')
# say_hello('Daniel', ':D')
# say_hello('Miruna', ':)')


# # keyword arguments
# say_hello(emoji=':D', name='Bibi')

# Default parameters and arguments

# def say_hello(name='Darth Vader', emoji=';)'):
#     print(f'Hello {name} {emoji}')
#
#
# say_hello()


# return ( return also exits the function)

# def sum(num1, num2):
#     return num1 + num2


#
# total = sum(10,5)
# print(sum(10, total))
# second option
# print(sum(10, (sum(10, 5))))  # removed the variable 'total' and write the code in one line only.


# A function should return something!


# ///////

# def sum(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2
#
#     return another_func(num1, num2)
#
#
# total = sum(10, 20)
# print(total)

# example of other nested funct with different parameters.
def calculator(num1, num2):
    def add(num3, num4):
        return num3 + num4

    def multiply(num3, num4):
        return num3 * num4

    result_add = add(num1, num2)
    result_multiply = multiply(num1, num2)
    return result_add, result_multiply


sum_result, product_result = calculator(10, 20)
print(f"Sum: {sum_result}, Product: {product_result}")


