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