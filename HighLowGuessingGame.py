import random

print("This program pick a random number between 1 and 100 and tells you "
      "if your guess is to high or to low until you guess it.")

num = random.randint(1,100)

guessing = True
while guessing:
    guess = int(input("What is you guess? -> "))
    if guess > num:
        print("To high!")
    elif guess < num:
        print("To low!")
    else:
        print("Nice, you got it!")
        guessing = False

