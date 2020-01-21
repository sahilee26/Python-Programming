import re

if re.search("inform", "we need to inform him with the latest information"):
    print("There is inform")
else:
    print("Not found")


if re.search("must", "we need to inform him with the latest information"):
    print("Must is there")
else:
    print("Not found")#  Generating an iterator:
#
# Generating an iterator is the simple process of finding out and reporting the starting and the ending index of the string. Consider the following example:

import re

Str = "we need to inform him with the latest information"

for i in re.finditer("inform.", Str):
    locTuple = i.span()
    print(locTuple)
# For every match found, the starting and the ending index is printed. Can you take a guess of the output that we get when we execute the above program? Check it out below.# Matching words with patterns:
#
# Consider an input string where you have to match certain words with the string. To elaborate, check out the following example code:
#

import re

Str = "Sat, hat, mat, pat"

allStr = re.findall("[shmp]at", Str)

for i in allStr:
    print(i)#Matching series of range of characters:


import re

Str = "sat, hat, mat, pat"

someStr = re.findall("[h-m]at", Str)

for i in someStr:
    print(i)# We have added a caret symbol(^) in the Regular Expression. What this does it negates the effect of whatever it follows. Instead of giving us the output of everything starting with h to m, we will be presented with the output of everything apart from that.
import re

Str = "sat, hat, mat, pat"

someStr = re.findall("[^h-m]at", Str)

for i in someStr:
    print(i)import re

Food = "hat rat mat pat at"

regex = re.compile("[r]at")

Food = regex.sub("food", Food)

print(Food)import re

randstr = "12345"

print("\d Matches:", len(re.findall("\d", randstr)))



# As you can see from the above output, d matches the integers present in the string. However if we replace it with D, it will match everything BUT an integer, the exact opposite of d.

randstr = "12345"

print(" \\D Matches:", len(re.findall("\D", randstr)))import re

randstr = '''
Delhi is
capital of 
India
'''

print(randstr)

regex = re.compile("\n")

randstr = regex.sub(" ", randstr)

print(randstr)# Practical Use Cases Of Regular Expressions
# # We will be checking out 3 main use-cases which are widely used on a daily basis. Following are the concepts we will be checking out:
# #
# # Phone Number Verification
# # E-mail Address Verification
# # Web Scraping
# # Let us begin this section of Python RegEx tutorial by checking out the first case.
# #
# # Phone Number Verification:
# #
# # Problem Statement – The need to easily verify phone numbers in any relevant scenario.
# #
# # Consider the following Phone numbers:
# #
# # 444-122-1234
# # 123-122-78999
# # 111-123-23
# # 67-7890-2019
# # The general format of a phone number is as follows:
# #
# # Starts with 3 digits and ‘-‘ sign
# # 3 middle digits and ‘-‘ sign
# # 4 digits in the end

import re

phn = "412-555-1212"

if re.search("\d{3}-\d{3}-\d{4}", phn):
    print("Valid phone number")
else:
    print("Invalid Phone Number")import urllib.request
from re import findall

url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)

html = response.read()

htmlStr = html.decode()
print(htmlStr)
pdata = findall("\([1-9]{3}\) \d{3}-\d{4}", htmlStr)

for item in pdata:
    print(item)# \   Used to drop the special meaning of character
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
import re

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))
import re

# '*' replaces the no. of occurrence of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))
from re import split

# '\W+' denotes Non-Alphanumeric Characters or group of characters
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of characters
# Spliting occurs at '12', '2016', '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))
import re

# Splitting will occurs only once, at '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))
import re

# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber".
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string
# Upon matching, 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE))

# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced.
print(re.sub('ub', '~*' , 'Subject has Uber booked already'))

# As count has been given value 1, the maximum times replacement occurs is 1
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE))

# 'r' before the patter denotes RE, \s is for start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))
# Python3 program to extract all the numbers from a string
import re

# Function to extract all the numbers from the given string
def getNumbers(str):
	array = re.findall(r'[0-9]+', str)
	return array

# Driver code
str = "adbv345hj43hvb42"
array = getNumbers(str)
print(*array)
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
print(lst)# A Python program to demonstrate working of re.match().
import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

	# We reach here when the expression "([a-zA-Z]+) (\d+)"
	# matches the date string.

	# This will print [14, 21), since it matches at index 14
	# and ends at 21.
	print("Match at index %s, %s" % (match.start(), match.end()))

	# We us group() method to get all the matches and
	# captured groups. The groups contain the matched values.
	# In particular:
	# match.group(0) always returns the fully matched string
	# match.group(1) match.group(2), ... return the capture
	# groups in order from left to right in the input string
	# match.group() is equivalent to match.group(0)

	# So this will print "June 24"
	print("Full match: %s" % (match.group(0)))

	# So this will print "June"
	print("Month: %s" % (match.group(1)))

	# So this will print "24"
	print("Day: %s" % (match.group(2)))

else:
	print("The regex pattern does not match.")
# A Python program to demonstrate working
# of re.match().
# re.match() : This function attempts to match pattern to whole string. The re.match function returns a match object on success, None on failure.
import re


# a sample function that uses regular expressions
# to find month and day of a date.
def findMonthAndDate(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print
        "Not a valid date"
        return

    print
    "Given Data: %s" % (match.group())
    print
    "Month: %s" % (match.group(1))
    print
    "Day: %s" % (match.group(2))


# Driver Code
findMonthAndDate("Jun 24")
print("")
findMonthAndDate("I was born on June 24")
#re.findall() : Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found (Source : Python Docs).

# A Python program to demonstrate working of
# findall()
import re

# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and 
			my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)

# This example is contributed by Ayush Saluja.


#End of Program#


#End of Program#

import re

if re.search("inform", "we need to inform him with the latest information"):
    print("There is inform")
else:
    print("Not found")


if re.search("must", "we need to inform him with the latest information"):
    print("Must is there")
else:
    print("Not found")
#End of Program#

#  Generating an iterator:
#
# Generating an iterator is the simple process of finding out and reporting the starting and the ending index of the string. Consider the following example:

import re

Str = "we need to inform him with the latest information"

for i in re.finditer("inform.", Str):
    locTuple = i.span()
    print(locTuple)
# For every match found, the starting and the ending index is printed. Can you take a guess of the output that we get when we execute the above program? Check it out below.
#End of Program#

# Matching words with patterns:
#
# Consider an input string where you have to match certain words with the string. To elaborate, check out the following example code:
#

import re

Str = "Sat, hat, mat, pat"

allStr = re.findall("[shmp]at", Str)

for i in allStr:
    print(i)
#End of Program#

#Matching series of range of characters:


import re

Str = "sat, hat, mat, pat"

someStr = re.findall("[h-m]at", Str)

for i in someStr:
    print(i)
#End of Program#

# We have added a caret symbol(^) in the Regular Expression. What this does it negates the effect of whatever it follows. Instead of giving us the output of everything starting with h to m, we will be presented with the output of everything apart from that.
import re

Str = "sat, hat, mat, pat"

someStr = re.findall("[^h-m]at", Str)

for i in someStr:
    print(i)
#End of Program#

import re

Food = "hat rat mat pat at"

regex = re.compile("[r]at")

Food = regex.sub("food", Food)

print(Food)
#End of Program#

import re

randstr = "12345"

print("\d Matches:", len(re.findall("\d", randstr)))



# As you can see from the above output, d matches the integers present in the string. However if we replace it with D, it will match everything BUT an integer, the exact opposite of d.

randstr = "12345"

print(" \\D Matches:", len(re.findall("\D", randstr)))
#End of Program#

import re

randstr = '''
Delhi is
capital of 
India
'''

print(randstr)

regex = re.compile("\n")

randstr = regex.sub(" ", randstr)

print(randstr)
#End of Program#

# Practical Use Cases Of Regular Expressions
# # We will be checking out 3 main use-cases which are widely used on a daily basis. Following are the concepts we will be checking out:
# #
# # Phone Number Verification
# # E-mail Address Verification
# # Web Scraping
# # Let us begin this section of Python RegEx tutorial by checking out the first case.
# #
# # Phone Number Verification:
# #
# # Problem Statement – The need to easily verify phone numbers in any relevant scenario.
# #
# # Consider the following Phone numbers:
# #
# # 444-122-1234
# # 123-122-78999
# # 111-123-23
# # 67-7890-2019
# # The general format of a phone number is as follows:
# #
# # Starts with 3 digits and ‘-‘ sign
# # 3 middle digits and ‘-‘ sign
# # 4 digits in the end

import re

phn = "412-555-1212"

if re.search("\d{3}-\d{3}-\d{4}", phn):
    print("Valid phone number")
else:
    print("Invalid Phone Number")
#End of Program#

import urllib.request
from re import findall

url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)

html = response.read()

htmlStr = html.decode()
print(htmlStr)
pdata = findall("\([1-9]{3}\) \d{3}-\d{4}", htmlStr)

for item in pdata:
    print(item)
#End of Program#

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

#End of Program#

import re

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

#End of Program#

import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))

#End of Program#

import re

# '*' replaces the no. of occurrence of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))

#End of Program#

from re import split

# '\W+' denotes Non-Alphanumeric Characters or group of characters
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of characters
# Spliting occurs at '12', '2016', '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

#End of Program#

import re

# Splitting will occurs only once, at '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))

#End of Program#

import re

# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber".
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string
# Upon matching, 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE))

# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced.
print(re.sub('ub', '~*' , 'Subject has Uber booked already'))

# As count has been given value 1, the maximum times replacement occurs is 1
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE))

# 'r' before the patter denotes RE, \s is for start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

#End of Program#

# Python3 program to extract all the numbers from a string
import re

# Function to extract all the numbers from the given string
def getNumbers(str):
	array = re.findall(r'[0-9]+', str)
	return array

# Driver code
str = "adbv345hj43hvb42"
array = getNumbers(str)
print(*array)

#End of Program#

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
#End of Program#


#End of Program#

# A Python program to demonstrate working of re.match().
import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

	# We reach here when the expression "([a-zA-Z]+) (\d+)"
	# matches the date string.

	# This will print [14, 21), since it matches at index 14
	# and ends at 21.
	print("Match at index %s, %s" % (match.start(), match.end()))

	# We us group() method to get all the matches and
	# captured groups. The groups contain the matched values.
	# In particular:
	# match.group(0) always returns the fully matched string
	# match.group(1) match.group(2), ... return the capture
	# groups in order from left to right in the input string
	# match.group() is equivalent to match.group(0)

	# So this will print "June 24"
	print("Full match: %s" % (match.group(0)))

	# So this will print "June"
	print("Month: %s" % (match.group(1)))

	# So this will print "24"
	print("Day: %s" % (match.group(2)))

else:
	print("The regex pattern does not match.")

#End of Program#

# A Python program to demonstrate working
# of re.match().
# re.match() : This function attempts to match pattern to whole string. The re.match function returns a match object on success, None on failure.
import re


# a sample function that uses regular expressions
# to find month and day of a date.
def findMonthAndDate(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print
        "Not a valid date"
        return

    print
    "Given Data: %s" % (match.group())
    print
    "Month: %s" % (match.group(1))
    print
    "Day: %s" % (match.group(2))


# Driver Code
findMonthAndDate("Jun 24")
print("")
findMonthAndDate("I was born on June 24")

#End of Program#

#re.findall() : Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found (Source : Python Docs).

# A Python program to demonstrate working of
# findall()
import re

# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and 
			my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)

# This example is contributed by Ayush Saluja.


#End of Program#


#End of Program#


#End of Program#

