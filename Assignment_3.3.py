gender = input("Enter your biological gender: ").lower()
hemoglobin_val = int(input("Enter your hemoglobin value: "))

if gender == "male":
    if hemoglobin_val < 134:
        print("hemoglobin value is low")
    elif hemoglobin_val > 167:
        print("hemoglobin value is high")
    else:
        print("hemoglobin value is normal")

if gender == "female":
    if hemoglobin_val < 117:
        print("hemoglobin value is low")
    elif hemoglobin_val > 155:
        print("hemoglobin value is high")
    else:
        print("hemoglobin value is normal")

