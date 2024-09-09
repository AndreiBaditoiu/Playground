from functools import reduce
# lambda expressions-Are one-time, anonymous functions that you use only once. It has this form:
# lambda param(item): (action it has to take) item*2
my_list = [1, 2, 3]


print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda x, y: x+y, my_list))