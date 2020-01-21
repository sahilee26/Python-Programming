#Matching series of range of characters:


import re

Str = "sat, hat, mat, pat"

someStr = re.findall("[h-m]at", Str)

for i in someStr:
    print(i)