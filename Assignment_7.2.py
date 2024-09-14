name_list = set()

while(True):
    name = input("Enter Name: ")
    if name == "":
        break
    elif name in name_list:
        print("Existing name")
    elif name not in name_list:
        print("New name")
        name_list.add(name)

for name in name_list:
    print(name)