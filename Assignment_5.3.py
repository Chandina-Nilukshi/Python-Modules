num = int(input("Enter the number: "))

prime = True

for i in range (2, num):
    if num % i == 0:
        prime = False
        break

if prime == True:
    print("Its a prime")
else:
    print("Not a prime")

