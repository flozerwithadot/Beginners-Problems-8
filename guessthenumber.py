import random

num = (random.randint(1, 100))

tries = 0

correct = False

while correct == False:
    guess = int(input("guess a number from 1 to 100 "))
    if guess > num:
     print("your guess is too high.")
     tries = tries + 1
    elif guess < num:
        print("your guess is too low")
        tries = tries + 1
    elif guess == num:
        correct = True

print(tries)
