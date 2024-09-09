# Collections module
from collections import OrderedDict, Counter, defaultdict
import datetime
from  time import time
# Counter
start = time()
li = [1, 2, 3, 4, 5, 6, 7, ]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))
#
# # # defaultdict
#
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c'])


# OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2


d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1


print(d2 == d)

print(datetime.date.today())
end = time()
print(f'it took {end - start:.2f} seconds')