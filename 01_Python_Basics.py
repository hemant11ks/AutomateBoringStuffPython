import random
import sys

# a = 2 + 3*6
# print(a)  # 20
#
# a1 = (2+3) * 6
# print(a1) # 30
from click import password_option

# print("Hi Hemant What is you age")
# myAge = input()
# print("Good to know your age is, " + str(int(myAge) + 1))

# If we use "print()" it will work as a blank line

# if condition print only one time
# spam = 0
# if spam < 3:
#     print("Hi ")
#     spam = spam + 1

# while condition print n times
# spam = 0
# while spam < 3:
#     print("Hi ")
#     spam = spam +1

# Break Statement

# while True:
#     print("Please type your name ")
#     name = input()
#     if name == 'Alex':
#         break
# print('Thankyou')

# Continue Statement

# while True:
#     print("Who are you ?")
#     name = input()
#     if name != 'Alex':
#         continue
#     print("Hi Alex what is the password ?")
#     password = input()
#     if password == '1234':
#         break
# print('Access Granted')

# for Loops and the range() function

# total = 0
# for i in range(5):
#     total = total + i
# print(total)  # 10

# Starting(First Arg), Stopping(Second Arg) and Stepping(Third Arg) Argument to range()

# for i in range(5,10):
#     print(i)
#  # 5 6 7 8 9

# for i in range(5, 10, 2):
#     print(i)
#     # 5 7 9

# for i in range(5, -1, -1):
#     print(i) # 5 4 3 2 1 0

# for i in range(5):
#     print(random.randint(1,8))
#

# from import Statements
# random import *.

# Exit program using sys.exit()

while True:
    print("Type EXIT if you want to exit")
    response = input()
    if response == 'EXIT':
        sys.exit()
    print('You types ' + response + '.')

