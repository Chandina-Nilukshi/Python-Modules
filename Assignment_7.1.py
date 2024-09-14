seasons = ("Spring", "Summer", "Autumn", "Winter")

month_num = int(input("Enter the number of the month: "))

if month_num in {12, 1, 2}:
    print(f"The season is {seasons[3]}")

elif month_num in {3, 4, 5}:
    print(f"The season is {seasons[0]}")

elif month_num in {6, 7, 8}:
    print(f"The season is {seasons[1]}")

elif month_num in {9, 10, 11}:
    print(f"The season is {seasons[2]}")
else:
    print("Invalid month entered")