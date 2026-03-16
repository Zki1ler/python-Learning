#problem 1

age = int(input("Enter your age: "))
matinee = input("Is this a matine showing? Yes/No: ").lower()

ismatinee = True if matinee == "yes" else False

if age < 0:
    print("ERROR")

elif age < 13:
    group = "Child"
    if ismatinee == True:
        price = 6.00
    else:
        price = 8.00

elif age <= 17:
    group = "Teen"
    if ismatinee == True:
        price = 7.00
    else:
        price = 10.00
    
elif age <= 64:
    group = "Adult"
    if ismatinee == True:
        price = 8.00
    else:
        price = 13.00

else:   
    group = "senior"
    if ismatinee == True:
        price = 6.00
    else:
        price = 7.00

print("age group:", group)
print(f"Ticket price: ${price:.2f}")

#problem 2
errors = []

student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

if len(student_id) != 8:
    errors.append(f"Student ID must be 8 characters long. (you have {len(student_id)})")

if not student_id[0].isalpha():
    errors.append("Student ID must start with a letter.")

if not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter.")

if len(name.strip()) < 2:
    errors.append("Name must be at least 2 characters long.")

try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99.")
except ValueError:
    errors.append("Age must be a valid integer.")

valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append(f"Major must be one of the following: CS, IT, CE, DS. (you entered {major})")

if len(errors) == 0:
    print("Profile is successfully created.")
    print (f"Student ID: {student_id}")
    print (f"Name: {name}")
    print (f"Age: {age}")
    print (f"Major: {major}")

else:
    print("Profile creation failed due to the following errors:")
    for e in errors:
        print(f"-", e)

#problem 3
print("===================================")
print("CAMPUS CAFÉ ORDER SYSTEM")
print("===================================")
print("==============================")
print("1. Coffee - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad - $5.50")
print("4. Combo - $8.00")
print("5. Exit")
print("==============================")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    size = input("Enter size (small/medium/large): ").lower()

    if size == "medium":
        price = 4.50
        item = "Medium Coffee"
    elif size == "large":
        price = 5.50
        item = "Large Coffee"
    else:
        price = 3.50
        item = "Small Coffee"
    
elif choice == "2":
    cheese = input("Add cheese? (yes/no): ").lower()

    if cheese == "yes":
        price = 6.75
        item = "Sandwich add Cheese"
    else:
        price = 6.00
        item = "Sandwich"
    
elif choice == "3":
    dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").lower()

    if dressing not in ["ranch", "italian", "vinaigrette", "none"]:
        print("Invalid dressing choice. Defaulting to 'none'.")
        dressing = "none"
    
    price = 5.50
    item = f"Salad ({dressing})"

elif choice == "4":
    size = input("Enter size (small/medium/large): ").lower()
    cheese = input("Add cheese? (yes/no): ").lower()

    coffee_price = 3.50
    if size == "medium":
        coffee_price = 4.50
    elif size == "large":
        coffee_price = 5.50
    
    sandwich_price = 6.00
    if cheese == "yes":
       sandwich_price += 0.75
    
    price = coffee_price + sandwich_price
    item = "Combo"

elif choice == "5":
    print("Goodbye!")

else:
    print("Invalid choice.")
    exit() 

name = input("Enter your name: ")
while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")  

try:
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        raise ValueError
except:
    print("Invalid quantity")
    exit()

subtotal = price * quantity
tax = subtotal * 0.07
total = subtotal + tax

print("===================================")
print("CAMPUS CAFÉ ORDER RECEIPT")
print("===================================")
print("Customer Name:", name)
print("Item Ordered:", item)
print("Quantity:", quantity)
print(f"Unit Price: ${price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("===================================")
print("Thank you for your order!")
