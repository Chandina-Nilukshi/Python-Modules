list = []
largest = None

while(True):
    num = input("Enter number: ")
    if num == "":
        break
    else:
        list.append(int(num))

list.sort(reverse=True)
print(list[0:5])