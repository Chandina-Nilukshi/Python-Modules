airports = {}

print("Choose an option")
print("1. Enter a new airport")
print("2. Fetch Information")
print("3. Quit")

while(True):
    option = input("Enter your option number: ")
    
    if option == "1":
        ICAO_code = input("Enter the ICAO code: ").upper()
        airport_name = input("Enter the airport name: ")
        airports[ICAO_code] = airport_name
        print("Airport was added")

    elif option == "2":
        ICAO_code = input("Enter the ICAO code: ").upper()
        if ICAO_code in airports:
            print(f"The airport having {ICAO_code} ICSAO code is {airports[ICAO_code]}")
        else:
            print("No information can be found")
    
    elif option == "3":
        print("Exiting")
        break

    else:
        print("Invalid option. Pls select a valid option")