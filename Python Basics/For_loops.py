# 'for' loops; it is used to iterate through something
# for item in 'Zero to Mastery':
#     print(item)
#
# for item in (1, 2, 3, 4, 5):
#     for x in ["a", "b", "c"]:
#         print(item, x)

# range()
# for _ in range(0, 10, 2):
#     print(_)
#
# print( )
# for i in range(2):
#     print(list(range(10)))


# enumerate()

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f'Index of 50 is: {i}')
