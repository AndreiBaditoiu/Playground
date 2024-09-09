some_list = ['a', 'b', 'c', 'd', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for i in some_list:
#     if some_list.count(i) > 1:
#         if i not in duplicates:
#             duplicates.append(i)
# print(duplicates)

duplicates = list(set([i for i in some_list if some_list.count(i) > 1]))
print(duplicates)
