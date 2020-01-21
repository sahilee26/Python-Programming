# \   Used to drop the special meaning of character
#     following it (discussed below)
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One ore more occurrences
# {}  Indicate number of occurrences of a preceding RE
#     to match.
# ()  Enclose a group of REs
# \d   Matches any decimal digit, this is equivalent
#      to the set class [0-9].
# \D   Matches any non-digit character.
# \s   Matches any whitespace character.
# \S   Matches any non-whitespace character
# \w   Matches any alphanumeric character, this is
#      equivalent to the class [a-zA-Z0-9_].
# \W   Matches any non-alphanumeric character.

# Module Regular Expression is imported using __import__().
import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))
