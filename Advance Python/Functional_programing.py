from functools import reduce

# Pure functions
# It has 2 rules:
# 1. Given the same input, it will always return the same output.
# 2. A function should not produce any side effects.


# def multiply_by2(li):
#     new_li = []
#     for item in li:
#         new_li.append(item * 2)
#     return new_li
#
#
# print(multiply_by2([1, 2, 3]))


# print(multiply_by2([1, 2, 3]))


# Useful functions for Functional Programming (FP)
# map(), filter(), zip() and reduce()

# my_list = [1, 2, 3]
#
#
# def multiply_by2(item):
#     return item * 2
#
#
# print(list(map(multiply_by2, my_list)))
# print(my_list)  # the above function doesn't touch/ change the outside list, it leaves it as it is;
# it will just create a new list .


# fiter()

# my_list = [1, 2, 3]

# def only_odd(item):
#     return item % 2 != 0
#
#
# print(list(filter(only_odd, my_list)))

new_list = ['Ana', 'Maria', 'Darius']


def initial_a(item):
    return item.startswith('A')


result = list(filter(initial_a, new_list))
print(result)

# zip()

# my_list = [1, 2, 3]
# your_list = (10, 20, 30)
# their_list = [5, 4, 6]
# our_list = {'a', 'b', 'c'}
#
# result = (list(zip(my_list, your_list, their_list, our_list)))
# print(result)
# print(type(our_list))
#
# # reduce()
my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
