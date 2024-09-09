# Type Conversion

# Convert int into str
# print(type(str(100)))

# A different way to do it ( convert into str and back to int
# a = str(100)
# b = int(a)
# c = type(b)
# print(c)


# Escape Sequence

# weather = "It\'s \"kind of\" sunny" # whatever comes after '\' Python will consider it a str
# print(weather)

# weather = "\t It\'s \"kind of\" sunny \n Hope you have a good day"  # '\t' will add a tab at the beginning;
# '\n will add a new line
# print(weather)

# Formatted Strings

# name = "Johnny"
# age = 55
# # print('Hi ' + name + '. You are ' + str(age) + ' years old.')
#
# # now the same thing but formatted
# print(f'Hi {name}. You are {age} years old.')

# String indexes
# selfish = '01234567'
#         #  01234567
# print(selfish[0:2])

# python = 'I am PYHTON'
#
# print(python[1:4])
# print(python[1:])
# print(python[:])
# print(python[1:100])
# print(python[-1])
# print(python[-4])
# print(python[:-3])
# print(python[-3:])
# print(python[::-1])

# Immutability -> in Python you cannot change parts of a str;
# only the entire str( as in entire variable) can be changed. You can't reassign parts of a string.
# "TypeError: 'str' object does not support item assignment".
# selfish = '01234567'
#         #  01234567
# selfish[3] = '8'
# name = 'Andrei'
# age = 50
# relationship_status = 'single'
# print(relationship_status)
#
# relationship_status = 'it\'s complicated'
#
# print(relationship_status)

# ///////

# birth_year = input('What year are you born in? ')
# birth_year = int(birth_year)
# current_year = datetime.now().year
# age = current_year - birth_year
# print(f'Your age is {age}')

# ///// option two:
# birth_year = int(input('What year are you born in? '))
# current_year = int(input('What is the current year? '))
# age = current_year - birth_year
# print(f'Your age is {age}')

# ////////// third option:

birth_year = input('What year are you born in? ')
age = 2024 - int(birth_year)
print(f'Your age is {age}')


