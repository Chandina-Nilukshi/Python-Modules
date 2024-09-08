def convert(gallons):
    return gallons * 3.7854

def main():
    while(True):
        gallons = int(input("Enter gasoline quantity in American gallons: "))
        if gallons < 0:
            break
        else:
            litres = convert(gallons)
            print(f"{gallons} American gallons is {litres} litres")

main()