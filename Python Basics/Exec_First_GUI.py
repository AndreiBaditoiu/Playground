# Exercise

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]

]


# for row in range(len(picture)):
#     for col in range(len(picture[0])):
#         if picture[row][col] == 1:
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print('')


def show_picture():
    for image in picture:
        for pixel in image:
            if pixel:
                print('*', end="")
            else:
                print(' ', end="")
        print('')


show_picture()
print('\n')
show_picture()
print('\n')
show_picture()
