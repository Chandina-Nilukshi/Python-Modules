smallest_num = None
largest_num = None
while (True):
    num = input("Enter a number: ")
    if num == "":
        break
    elif smallest_num is None or int(num) < smallest_num:
        smallest_num = int(num)
    elif largest_num is None or int(num) > largest_num:
        largest_num = int(num)

print(f"The smallest number is {smallest_num}")
print(f"The largest number is {largest_num}")