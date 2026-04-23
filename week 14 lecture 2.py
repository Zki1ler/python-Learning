roygb = (255, 128, 0)
print(f"red: {roygb[0]}")
print(f"green: {roygb[1]}")
print(f"blue: {roygb[2]}")
palette = []
palette.append(roygb)
print (palette)

#Create your RGB color tuple here
# Print each color channel
# Create palette list and add color
# Print the palette

student1 = ("Alice", 91, 20)
student2 = ("Bob", 85, 22)
student3 = ("Carol", 78, 19)

classroom = [student1, student2, student3]
print(f"Second student: {classroom[1][0]}")

name, grade, age = classroom[0]

print(f"{name} is {age} years old and earned a grade of {grade}.")

student = ("Alice", [88, 92, 79], "B")
print(f"Originial: {student}")

student[1].append(95)

exams = student[1]
new_avg = sum(exams) / len(exams)

if new_avg >= 90:
    new_grade = "A"
elif new_avg >= 80:
    new_grade = "B"
elif new_avg >= 70:
    new_grade = "C"
elif new_avg >= 60:
    new_grade = "D"
else:
    new_grade = "F"

updated_student = (student[0], student[1], new_grade)

print(f"After 4th exam: {student}")
print(f"Updated tuple: {updated_student}")
print(f"New average: {new_avg:.2f}, New grade: {new_grade}")

homework_grades = [82, 76, 90]

todays_date = (4, 23, 2026)

def boost_grades(grades, bonus = 5):
    for i in range(len(grades)):
        grades[i] += bonus

print(f"Before boost: {homework_grades}")
boost_grades(homework_grades)
print(f"After Boost: {homework_grades}")
print(f"Todays date: {todays_date}")

def find_range(*args):
    if not args:
        return (None, None)
    return (min(args), max(args))

print(find_range(4, 17, 9))
print(find_range(3, 41, 7, 19, 55, 2, 28)) 

test_scores = [78, 92, 85, 88, 91]
print(find_range(*test_scores))


def calculate_statistics(*args):
    count = len(args)
    total = sum(args)
    average = total / count if count > 0 else 0.0
    return (count, total, average)

def update_student_records(students, bonus):
    updated = []
    for name, grade in students:
        new_record = (name, grade + bonus)   # new tuple — can't edit old one
        updated.append(new_record)
    return updated

roster = [("Alice", 88), ("Bob", 74), ("Carol", 91), ("Dan", 65)]
print(f"Original records: {roster}")

updated_roster = update_student_records(roster, 5)
print(f"Updated records:  {updated_roster}")
print(f"Original unchanged: {roster}") 

all_grades = [grade for _, grade in roster]
stats = calculate_statistics(*all_grades)
count, total, avg = stats
print(f"\nClass statistics:")
print(f"  Count:   {count}")
print(f"  Sum:     {total}")
print(f"  Average: {avg:.2f}")

updated_grades = [grade for _, grade in updated_roster]
u_count, u_total, u_avg = calculate_statistics(*updated_grades)
print(f"\nPost-bonus statistics:")
print(f"  Count:   {u_count}")
print(f"  Sum:     {u_total}")
print(f"  Average: {u_avg:.2f}")



grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Full grid: {grid}")

print(f"Center number: {grid[1][1]}")

print("\nFormatted grid:")
for row in grid:
    for value in row:
        print(value, end=" ")
    print()

student_scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

passing_grades = [g for g in student_scores if g >= 60]

letter_grades = [
    "A" if g >= 90 else
    "B" if g >= 80 else
    "C" if g >= 70 else
    "D"
    for g in passing_grades
]

print(f"All scores:     {student_scores}")
print(f"Passing grades: {passing_grades}")
print(f"Letter grades:  {letter_grades}")



mult_table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

print("4x4 Multiplication Table:")
print(f"{'':>4}", end="")
for col in range(1, 5):
    print(f"{col:>4}", end="")
print()
print("    " + "----" * 4)
for i, row in enumerate(mult_table, 1):
    print(f"{i:>3}|", end="")
    for val in row:
        print(f"{val:>4}", end="")
    print()

def sum_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


diagonal_sum = sum_diagonal(mult_table)
print(f"\nDiagonal elements: {[mult_table[i][i] for i in range(4)]}")
print(f"Diagonal sum: {diagonal_sum}")

even_gen = (val for row in mult_table for val in row if val % 2 == 0)

print("\nFirst 5 even numbers from the table:")
count = 0
for val in even_gen:
    print(val, end="  ")
    count += 1
    if count == 5:
        break
print()