cabin_cls = input("Pls enter the cabin cls: ")
if cabin_cls == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin_cls == "A":
    print("above the car deck, equipped with a window")
elif cabin_cls == "B":
    print("windowless cabin above the car deck")
elif cabin_cls == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")