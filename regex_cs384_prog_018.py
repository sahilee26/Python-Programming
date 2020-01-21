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
