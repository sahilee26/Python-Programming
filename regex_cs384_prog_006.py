import re

Food = "hat rat mat pat at"

regex = re.compile("[r]at")

Food = regex.sub("food", Food)

print(Food)