import re

file = open("text.txt", "r")
# print(file.read())
latin = re.findall('[a-zA-Z]', file.read())
for x in latin:
    latin[latin.index(x)] = x.lower()
print(latin)
chars = []
for i in latin:
    if i not in chars:
        chars.append(i)
print(chars)
