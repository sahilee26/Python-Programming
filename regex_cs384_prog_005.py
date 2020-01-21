# We have added a caret symbol(^) in the Regular Expression. What this does it negates the effect of whatever it follows. Instead of giving us the output of everything starting with h to m, we will be presented with the output of everything apart from that.
import re

Str = "sat, hat, mat, pat"

someStr = re.findall("[^h-m]at", Str)

for i in someStr:
    print(i)