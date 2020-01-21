import re

if re.search("inform", "we need to inform him with the latest information"):
    print("There is inform")
else:
    print("Not found")


if re.search("must", "we need to inform him with the latest information"):
    print("Must is there")
else:
    print("Not found")