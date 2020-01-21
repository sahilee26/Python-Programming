#  Generating an iterator:
#
# Generating an iterator is the simple process of finding out and reporting the starting and the ending index of the string. Consider the following example:

import re

Str = "we need to inform him with the latest information"

for i in re.finditer("inform.", Str):
    locTuple = i.span()
    print(locTuple)
# For every match found, the starting and the ending index is printed. Can you take a guess of the output that we get when we execute the above program? Check it out below.