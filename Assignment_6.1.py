import random
def dice():
    return random.randint(1, 6)

def main():
    while(True):
        result = dice()
        print(f"Rolled a {result}")
        if result == 6:
            break

main()