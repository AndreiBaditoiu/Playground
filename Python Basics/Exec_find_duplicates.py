# Check for duplicates in the list
from collections import Counter

some_list = ['a', 'b', 'c', 'd', 'b', 'd', 'm', 'n', 'n']

# Solution 1

counter = Counter(some_list)
duplicates = [item for item, count in counter.items() if count > 1]
if duplicates:
    print('Duplicates found', duplicates)

# Solution 2
duplicates = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)
