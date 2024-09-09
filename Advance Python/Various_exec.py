"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


# range; build a function to keep cod clean and readable!!

def filter_func(start, end):
    my_ls = []
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            my_ls.append(i)

    for index, value in enumerate(my_ls):
        if index < len(my_ls) - 1:
            print(value, end=',')
        else:
            print(value)


filter_func(2000, 3200)

# list comprehensions

# print(*(i for i in range(2000, 3200) if i % 7 == 0 and i % 5 != 0 ), sep=',')

# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")
