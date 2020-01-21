# Matching words with patterns:
#
# Consider an input string where you have to match certain words with the string. To elaborate, check out the following example code:
#

import re

Str = "Sat, hat, mat, pat"

allStr = re.findall("[shmp]at", Str)

for i in allStr:
    print(i)