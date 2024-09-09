# my_string = "Hello World"
# for char in my_string:
#     print(char)

# iterable can be a list, a dict, a str, a set

# my_set = (1, 2, 3)
# for num in my_set:
#     print(num)

# iterate = go through each element, one by one and check all items in a collection.

# iterate through a dict

user = {
    'name': 'Golem',
    'age': 5000,
    'can_swim': False
}
for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# for key, value in user.items():
#     print(key, value)
for k, v in user.items(): # same as above; k = key, v = value.
    print(k, v)
