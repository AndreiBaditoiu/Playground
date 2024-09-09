#  set; Sets are used to store multiple items in a single variable;
#  They are unordered collection of unique objects/items
# my_set = {1, 2, 3, 4, 5}  # it has no duplicates
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# my_list = [1, 2, 3, 4, 5, 5]
# my_set = set(my_list)
# print(my_set)
# # they don't support indexing.
# print(1 in my_set)
# print(len(my_set))
# print(list(my_set))
#
# # .copy()
# new_set = my_set.copy()
# my_set.clear()
# print(new_set)
# print(my_set)

# Methods

my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(your_set)) # finds the difference between the two sets
# print(my_set.discard(5)) # discards/deletes an element if it exists
# print(my_set)
# print(my_set.difference_update(your_set)) # Removes all elements of another set from this set.
# print(my_set)
# print(my_set.intersection(your_set)) # Finds common elements in two sets.
# Also, '&' can be used instead of .intersection()

# print(my_set.isdisjoint(your_set)) # Checks if the two sets have nothing in common
# print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))
# union()
# print(my_set | your_set)  # union() creates a single set from the two given; Also '|' does the same( shorthand)
