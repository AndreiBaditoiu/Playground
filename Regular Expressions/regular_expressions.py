import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Andrei'
a = pattern.search(string)

print(a)

# regular expressions II

""" A password,
8 characters long;
contains any sort of letters, numbers, punctuation;
has to end with a number.
"""
password = 'super874secret%$#8'
pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
check = pattern.fullmatch(password)
print(check)