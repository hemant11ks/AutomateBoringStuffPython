import re
# Basic Phone number check code:

# def isPhoneNumber(text):
#     if len(text)!=12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#         if text[3] != '-':
#             return False
#         for i in range(4,7):
#             if not text[i].isdecimal():
#                 return False
#         if text[7] != '-':
#             return False
#         for  i in range(8,12):
#             if not text[i].isdecimal():
#                 return False
#         return True
#
# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print(isPhoneNumber('415-WRONG-4242'))

# REGEX Pattern matching

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d') # re.compile() function used to create regex object.
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print('Phone number found: ' + mo.group()) # group() used to return the string of actual matched text.

# Grouping with Parenthesis
# Example: create groups in regex -> (d\d\d)-(\d\d\d-\d\d\d\d\)
# We can pass integer 1 or 2 to group() match object method

# It can't run we need to pass integer
# mo.groups()
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

#
# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My phone number is (415) 55-4242.')
# print(mo.group(1))
# print(mo.group(2))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())  # Batmobile
print(mo.group(1)) # mobile
























