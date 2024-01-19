import random

def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

print("This program pick a random number between 1 and 100 and tells you "
      "if your guess is to high or to low until you guess it.")

x = input("Enter the drawing range [1-x] -> ")
if is_integer(x):
    x = int(x)
    if x > 1:
        num = random.randint(1,x)

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
    else:
        print("Bad choice!")
else:
    print('You need to enter integer value!')

