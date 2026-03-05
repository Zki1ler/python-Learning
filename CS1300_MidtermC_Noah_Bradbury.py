##problem 1
Distance = float(input("Enter the distance: "))
scale = input("Enter unit (Km/Mi):").lower()

if scale == "km":
    mi = Distance * .0621371
    print(f"{Distance} km =  {mi} Miles")
elif scale == "mi":
    km = Distance * 1.60934
    print(f"{Distance} Miles =  {km} Km")
else:
    print("Invalid scale.")

##problem 2
sentence = input("Enter a sentence: ")

numcharacters = len(sentence)
num_words = len(sentence.split())

vowels = "aeiouAEIOU"
num_vowels = sum(1 for char in sentence if char in vowels)

constants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
num_constants = sum(1 for char in sentence if char in constants)

average_word_length = numcharacters / num_words

longest_word = max(sentence.split(), key=len)


print(f"Number of characters: {numcharacters}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {num_vowels}")
print(f"Number of constants: {num_constants}")
print(f"Average word length: {average_word_length:.2f}")
print(f"Longest word: {longest_word}")

##problem 3

assignments = ["Quiz1", "Homework1", "Lab 1", "Project 1", "Exam 1"]
scores = [85, 92, 78, 88, 95]

original_grade_book = dict(zip(assignments, scores))
print("Original Grade Book:", original_grade_book)

originalsorted_grade_book = dict(sorted(original_grade_book.items()))
print("Original Highest Grade: ", list(originalsorted_grade_book.values())[-1])
print("Original Lowest Grade: ", list(originalsorted_grade_book.values())[0])

originalaverage_grade = sum(originalsorted_grade_book.values()) / len(originalsorted_grade_book)
print("Original Average Grade: ", f"{originalaverage_grade:.2f}")

if originalaverage_grade >= 90:
    grade = "A"
elif originalaverage_grade >= 87:
    grade = "A-"
elif originalaverage_grade >= 83:
    grade = "B+"
elif originalaverage_grade >= 80:
    grade = "B"
elif originalaverage_grade >= 77:
    grade = "B-"
elif originalaverage_grade >= 73:
    grade = "C+"
elif originalaverage_grade >= 70:
    grade = "C"
elif originalaverage_grade >= 67:
    grade = "C-"
elif originalaverage_grade >= 63:
    grade = "D+"
elif originalaverage_grade >= 60:
    grade = "D"
else:
    grade = "F"



##problem 4

weight = float(input("Enter your weight in pounds: "))
Destination = input("Enter your destination (domestic/international): ").lower()
Premium = input("Premium member? (yes/no): ").lower()

if Destination == "domestic" and weight <= 5:
    if Premium == "yes":
        cost = 5.00 / 2 
    else:
        cost = 5.00
elif Destination == "domestic" and weight > 5:
    if Premium == "yes":
        cost = (5.00 + 0.75 * (weight - 5)) / 2
    else:
        cost = 5.00 + 0.75 * (weight - 5)
elif Destination == "domestic" and weight > 20:
    if Premium == "yes":
        cost = 16.25 + 0.50 * (weight - 20) / 2
    else:
        cost = 16.25 + 0.50 * (weight - 20)
elif Destination == "international" and weight <= 5:
    if Premium == "yes":
        cost = 15.00 / 2
    else:
        cost = 15.00
elif Destination == "international" and weight > 5:
    if Premium == "yes":
        cost = (15.00 + 2.00 * (weight - 5)) / 2
    else:
        cost = 15.00 + 2.00 * (weight - 5)
elif Destination == "international" and weight > 20:
    if Premium == "yes":
        cost = 45.00 + 1.50 * (weight - 20) / 2
    else:
        cost = 45.00 + 1.50 * (weight - 20)

print("*** Shipping Label ***")
print(f"Weight: {weight} lbs")
print(f"Destination: {Destination}")
print(f"Premium Member: {Premium}")
print(f"Cost: ${cost:.2f}")
print("***************************")

