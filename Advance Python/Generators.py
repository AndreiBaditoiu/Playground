"""Generators allow us to generate a sequence of values over time.
The special key word is 'yield'.
It can pause and
resume functions"""


# range(1000) range is a generator

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result
#
#
# my_list = make_list(100)
# print(my_list)

def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(10)
next(g)
next(g)
print(next(g))

# print(next(g))
# for item in generator_function(1000):
#     print(item)


