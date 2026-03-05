#problem 1
temp = float(input("Enter the temperature: "))
scale = input("Enter scale (c/f):").lower()

if scale == "c":
    f = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {f}")
elif scale == "f":
    c = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {c}")
else:
    print("Invalid scale.")

#problem 2
sent = input("Enter a sentence: ")

total = len(sent)

upper = 0
lower = 0
nums = 0
spaces = 0

for char in sent:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        nums += 1
    elif char.isspace():
        spaces += 1

print(f"Total characters: {total}")
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {nums}")
print(f"Spaces: {spaces}")
print("Reversed sentence:", sent[::-1])

##problem 4
gpa = float(input("Enter your GPA: "))
credits = int(input("Enter credit hours completed: "))
prereqs = input("prerequisites completed yes/no:")

if gpa >= 3.5 and credits >= 60 and prereqs.lower() == "yes":
    print("You are eligible to enroll in the course.")
elif gpa >= 3.5 and credits >= 60 and prereqs.lower() == "no":
    print("You are not eligible to enroll in the course. You need to complete the prerequisites.")
elif gpa >= 3.5 and credits >= 45:
    print("You are Waitlisted: you may be admitted if space is available.")
elif gpa >= 2.0:
    print("Not eligible yet: Raise your GPA or earn more credits.")
else:
    print("Denied: GPA is below minimum threshold.")