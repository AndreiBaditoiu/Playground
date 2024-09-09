# A list is a ordered sequence of objects, of any type.
# li = [1,2,3,4,5,6,7,8,9,10]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2.5, 3,'a', 'b', 'c', True]

# amazon_cart = ['notebooks',
#                'sunglasses',
#                'toys',
#                'grapes'
#                ]
# # print(amazon_cart[0])
# print(amazon_cart[1])

# Lists slicing
# print(amazon_cart[0::2])  # '::" = step over
# lists are mutable (elements in lists can be changed)
# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

# //////////// Exec.

# new_list = ['a', 'b', 'c']
# print(new_list[1])  # b
# print(new_list[-2])  # b
# print(new_list[1:3])  # b, c
# new_list[0] = 'z'
# print(new_list)  # [ z, b, c]
#
# my_list = [1, 2, 3]
# bonus = my_list + [5]
# my_list[0] = 'z'
# print(my_list)  # [z,2, 3]
# print(bonus)  # [1, 2, 3, 5]
# # All correct

# Lists Methods
# adding methods
# basket = [1, 2, 3, 4, 5]
# basket.append(100)  # appends an item at the end of a list
# new_list = basket
# print(new_list)
# basket.insert(5, 37)  # inserts an item at a specific index of a list
# print(basket)
# basket.extend([100, 200, 300])  # adds item/s at the end of the list
# print(basket)
#

#  removing methods

# basket = [1, 2, 3, 4, 5]
# basket.pop()  # without specified index removes the last item in the list; if given index, removes item at that index.
# basket.remove(4)  # removes a certain item/value from list
# basket.clear()  # empties a list
# print(basket)


#  index
# basket = ['a', 'b,', 'c', 'd', 'e', 'd']
#
# print(basket.index('d'))  # prints the index of a specified element
# print(basket.count('d'))  # prints the index of a specified element
# print('d' in basket)

# sort
# basket = ['a', 'b,', 'c', 'd', 'e', 'd']
# basket.sort()
# print(basket)
# print(sorted(basket))
# basket.reverse()
# print(basket)


# range
# print(list(range(1, 100)))

# join (for str)


# new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'my', 'JOJO'])
# print(new_sentence)

# list unpacking

a, b, c, *other, d = [1, 2, 3, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
