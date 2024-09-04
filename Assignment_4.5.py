tries = 1

while(True):
    username = input("Username: ")
    password = input("Password: ")
    
    if username == "python" and password == "rules":
        print("Welcome")
        break
    elif tries == 5:
        print("Access Denied")
        break
    else:
        print("Enter the password again")
        tries += 1
