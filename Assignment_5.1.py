import random

dice = int(input("No. of dice to roll: "))
sum = 0

for i in range(dice):
    face = random.randint(1, 6)
    sum += face

print(f"The sum is {sum}")
