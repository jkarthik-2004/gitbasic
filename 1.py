import re
password = input("Enter the password: ")
if len(password) < 8:
    print("Invalid Password")
    exit()
if not re.search("[a-z]", password):
    print("Invalid Password")
    exit()
if not re.search("[A-Z]", password):
    print("Invalid Password")
    exit()
if not re.search("[0-9]", password):
    print("Invalid Password")
    exit()
if not re.search("[@#$%]", password):
    print("Invalid Password")
    exit()
if re.search("\s", password):
    print("Invalid Password")
    exit()
    
print("Valid Password")
