def unit_price(diameter, price):
    area = 3.14 * (diameter/2) ** 2
    unit_cost = price / area
    return unit_cost

def main():
    pizza1_diameter = int(input("Diameter of the pizza option 1 in centimeters: "))
    pizza1_prize = int(input("Prize of the pizza option 1 in euros: "))

    option_1 = unit_price(pizza1_diameter, pizza1_prize)

    pizza2_diameter = int(input("Diameter of the pizza option 2 in centimeters: "))
    pizza2_prize = int(input("Prize of the pizza option 2 in euros: "))

    option_2 = unit_price(pizza2_diameter, pizza2_prize)

    print(f"The unit prize of option 1 pizza is {option_1:.2f}")
    print(f"The unit prize of option 2 pizza is {option_2:.2f}")

    if option_1 < option_2:
        print("Option 1 you entered gives better value for money")
    elif option_2 < option_1:
        print("Option 2 you entered gives better value for money")
    else:
        print("Both options offers the same value for money")

main()

