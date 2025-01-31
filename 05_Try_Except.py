# def div42By(dividedby):
#     try:
#         return 42 / dividedby
#     except ZeroDivisionError:
#         print("You try to divide it by Zero")
#
# print(div42By(2))
# print(div42By(0))

# 21.0
# You try to divide it by Zero
# None -> Because of no return

# print("How many cats you have?")
# numCats = input()
#
# if int(numCats) >= 4:
#     print('That is a lot of cats')
# else:
#     print("That is not many cats")

# This code will fail when I give value in string like "6"

print("How many cats you have?")
numCats = input()

try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else:
        print("That is not many cats")
except ValueError:
    print("You did not enter a number!")


















