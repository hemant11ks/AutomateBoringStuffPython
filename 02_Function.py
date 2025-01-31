import random

from pycparser.c_ast import Assignment
from torch.autograd import variable

# def with parameters

# def hello(name):
#     print("Hi my name is " + name)
# hello('Alex')
#
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return "Omg"
#     elif answerNumber == 2:
#         return "Oops"
#     elif answerNumber == 3:
#         return "Wtf"
#
# r = random.randint(1,3)
# fortune = getAnswer(r)
# print(fortune)


# def spam():
#     eggs = 100
#     bacon()
#     print(eggs)
#
# def bacon():
#     ham = 200
#     eggs = 300
#
# spam() # 100
# Local variables are independent of each function
# Assignment statement = Local variable
# No assignment statement = Global variable

# Let's Discuss how to change the value of Global Variable

# def spam():
#     global eggs
#     eggs = "Changed"
#     print(eggs)
#
# eggs = 100
# spam()
# print(eggs)
