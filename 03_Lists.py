# spam = [['cat', 'bat'], [10,20,30]]
# print(spam[0])
# print(spam[0][0])
# print(spam[0][1])
# print(spam[1][2])

# ['cat', 'bat']
# cat
# bat
# 30
# It will give error due to out of range
# print(spam[0][4])

# Iterating from end of the list
# ls = [1,2,3,4]
# print(ls[-1]) # 4

# Getting sublist and slices

# spam[2] : is a list with an index
# spam[1:4] : is a list with a slice (two integers)

# In slice first int is where the slice will start and the second integer is where the slice will end

# spam = ['a', 'b', 'c', 'd']
# print(spam[0:2])
# print(spam[0:-2])
#
# ['a', 'b']
# ['a', 'b']

# As a shortcut we can also leave one param like:
# spam = ['cat', 'dog', 'bat', 'elephant']
# print(spam[:2])
# # ['cat', 'dog']
# print(spam[1:])
# # ['dog', 'bat', 'elephant']


# common list methods

# Lists are also objects in Python, and thus have methods that we can invoke on them. Here are a few that may be particularly useful (run help(list) in the python interpreter to see the full set):
# list method 	result
# append(item) 	add item to end of list
# extend(L1) 	add list L1 to original list
# sort() 	sort the list
# reverse() 	reverse the list
# count(item) 	return number of occurrences of item in list
# index(item) 	return index of first occurrence of item
# pop(index) 	remove and return item at index

# print('Hello' * 3)
# print([1,2,3] + [4,5,6])
# print([1,2,3] * 3)
# print(list('Hello'))

# HelloHelloHello
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
# ['H', 'e', 'l', 'l', 'o']

# var1 = 'hemant' in ['hemant', 'kumar', 'singh']
# print(var1) # True

# var2 = 'hemant' not in ['hemant', 'kumar', 'singh']
# print(var2) # False

# For loops with list, multiple assignment, and the Augmented Assignment operators

# print(range(4))
# print(list(range(4))) # [0,1,2,3]

# for i in range(4):
#     print(i)

# for i in [0,1,2,3]:
#     print(i)

# bucket = ['apples', 'oranges', 'cats', 'dogs']

# for i in range(len(bucket)):
#     print('Bucket ' + str(i) + ' is ' + bucket[i])

# Multiple Assignment
# cat = ['fat', 'orange', 'loud']
# size, color, disposition = cat
# print(size)
# print(color)
# print(disposition)
# fat
# orange
# loud

# size, color, disposition = 'fat', 'orange', 'loud'
# print(size)
# print(color)
# print(disposition)  

# Swapping variables
# a = 'AAA'
# b = 'BBB'
# a, b = b, a
# print(a)

#  BBB
# Augumented Assignment
# spam = 42
# spam = spam + 1

# spam += 1










