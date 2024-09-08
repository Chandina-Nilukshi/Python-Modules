import random
def dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice you want to roll: "))
    while (True):
        result = dice(sides)
        print(f"Rolled a {result}")
        if result == sides:
            break

main()