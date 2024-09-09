# List, sets, dictionary comprehensions (a method to construct lists, sets, dictionaries).

# The 'for' loop method:
# my_list = []
#
# for char in 'Hello':
#     my_list.append(char)
#
# print(my_list)

# List comprehensions method: it is in this form  "my_list = ['parameter' for 'parameter' in 'iterable']"
# my_list = [char for char in 'Hello']
# print(my_list)
#
# my_list2 = [item * 2 for item in range(0, 100)]
# print(my_list2)
#
# my_list4 = [item ** 2 for item in range(0, 100) if item % 2 == 0]
# print(my_list4)

# set and dictionaries comprehensions
# sets comprehensions
my_list = {char for char in 'Hello'}
print(my_list)

# dictionary comprehension

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k: v ** 2 for k, v in simple_dict.items()}
print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)