import random

print("Hello, What is your name? ")
name = input()

print("Well, " + name + ", I am thinking number between 1 to 20")
secretNumber = random.randint(1, 20)


# print('DEBUG: Secret number is ' + str(secretNumber))

for guessTaken in range(1, 7):
    print('Take a guess. ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low. ')
    elif guess > secretNumber:
        print('Your guess is too high. ')
    else:
        break # This condition for the correct guess!
if guess == secretNumber:
    print('Good job, ' + name + ' You guessedmy number')
else:
    print('Nope. The number I was thinking was ' + str(secretNumber))
      