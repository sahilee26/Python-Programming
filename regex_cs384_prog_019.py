# $	Matches the end of the line
# \s	Matches whitespace
# \S	Matches any non-whitespace character
# *	Repeats a character zero or more times
# \S	Matches any non-whitespace character
# *?	Repeats a character zero or more times (non-greedy)
# +	Repeats a character one or more times
# +?	Repeats a character one or more times (non-greedy)
# [aeiou]	Matches a single character in the listed set
# [^XYZ]	Matches a single character not in the listed set
# [a-z0-9]	The set of characters can include a range
# (	Indicates where string extraction is to start
# )	Indicates where string extraction is to end

import re

# Example string
s = 'Hello from shubhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM'

# \S matches any non-whitespace character
# @ for as in the Email
# + for Repeats a character one or more times
lst = re.findall('\S+@\S+', s)

# Printing of List
print(lst)