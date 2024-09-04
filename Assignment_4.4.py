import random
number = random.randint(1, 10)

while(True):
    guess = int(input("What is your guess?: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct")
        break