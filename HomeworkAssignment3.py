num1 = eval(input("Enter first number a: "))
num2 = eval(input("Enter second number b: "))
num3 = eval(input("Enter third number c: "))

expression1 = num1 < num2 < num3

expression2 = not(num1 > num2 or num2 > num3)

expression3 = num1 <= num2 and num2 <= num3

print("a < b < c:", expression1)
print("not(a > b or b > c):", expression2)
print("a <= b and b <= c:", expression3)

if expression2 == expression3:
    print("De Morgan's law holds true: B and C are a match")

else:
    print("De Morgan's law does not hold true: B and C are not a match")

# problem 2
temp = eval(input("Enter a temperature in Fahrenheit: "))
raining = input("Is it raining? (yes/no): ").lower()

if temp > 100:
    print("It's too hot to go outside.")

elif temp > 85:
    if raining == "yes":
        print("It's hot and raining. Better watch out for flooding.")
    else:
        print("It's hot and dry outside. You can go outside but make sure to stay hydrated.")

elif 60 <= temp <= 85:
    if raining == "yes":
        print("It's a nice temperature but it's raining. make sure to bring an umbrella.")
    else:
        print("It's a nice temperature and it's not raining. Have a great day outside!")

elif 32 <= temp < 60:
    print("It's a bit chilly outside. Make sure to wear a jacket.")

else:
    print("Freezing Temperature! Watch out for ice!")


# problem 3
name = input("Enter Student Name: ")

exam1 = float(input("Enter Exam 1 Score: "))
exam2 = float(input("Enter Exam 2 Score: "))
exam3 = float(input("Enter Exam 3 Score: "))

average = (exam1 + exam2 + exam3) / 3

if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Passing"
elif average >= 60:
    status = "Probation"
else:
    status = "suspension warning"

print("===============================")
print("Student Grade Report")
print("===============================")
print(f"Name: {name}")
print(f"Exam 1 Score: {exam1}")
print(f"Exam 2 Score: {exam2}")
print(f"Exam 3 Score: {exam3}")
print("===============================")
print(f"Average Score: {average:.2f}")
print(f"Letter Grade: {grade}")
print(f"Status: {status}")
print("===============================")
             
