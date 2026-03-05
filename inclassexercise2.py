##Beginner

age = int(input("Enter Your Age: "))

if 0 < age < 120:
    print("Valid age")


else:
    print("Invalid age")

pnumber = input("Enter Your Phone Number: ")

nospaces = len(pnumber.replace(" ", ""))
nodashes = len(pnumber.replace("-", ""))

if nospaces == 10 and nodashes == 10:
    print("Valid phone number")

else:
    print("Invalid phone number")

