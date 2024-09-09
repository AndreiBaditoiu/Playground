# It's a data type but also a data structure; they contain pairs of keys and values. Distinctive sign '{}'.
# dictionary = {
#     'a': [1, 2, 3],
#     'b': 'hello',
#     'c': True,
# }
#
# my_list = [{'a': [1, 2, 3],
#             'b': 'hello',
#             'c': True, },
#            {'a': [4, 5, 6],
#             'b': 'hello',
#             'c': True, }]
#
# print(my_list[0]['a'][2])

# dictionaries keys

# dictionary = {
#     123: [1, 2, 3],
#     True: ['Hello', 'World'],
#     '[1]': '200'
# }
# print(dictionary[123])
# print(dictionary[True])
# print(dictionary['[1]'])
# A key for a value should be something descriptive, like a str for example.


# Dictionaries methods
#  .get() = checks the presence of a key
user = {
    'basket': [1, 2, 3],
    'greet': ['Hello'],
    'age': 20
}
# print(user.get('age'))

# user2 = dict(name='John')
# print(user2)

# 'in'
# print('basket' in user)

# keys, values, items: iterates in keys and/ or in values; 'items checks bot keys and values.
# "items method will generate a tuple!!!
# print('age' in user.keys())
# print(20 in user.values())
# print(user.items())

# .clear() clears the whole dict.

# .copy() Copies the original dict.

# .pop() removes a certain key and value from the dict.
# print(user.pop('age'))
# print(user)

# .popitem() removes the last item in a dict.

# print(user.popitem())
# print(user)


# .update()  Updates a key/value in a dict.
print(user.update({'age': 55}))
print(user.update({'ages': 100}))
print(user)
