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