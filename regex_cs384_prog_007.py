import re

randstr = "12345"

print("\d Matches:", len(re.findall("\d", randstr)))



# As you can see from the above output, d matches the integers present in the string. However if we replace it with D, it will match everything BUT an integer, the exact opposite of d.

randstr = "12345"

print(" \\D Matches:", len(re.findall("\D", randstr)))