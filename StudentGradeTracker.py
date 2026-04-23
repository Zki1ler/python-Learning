def get_student_name():
    return input("Name of Student: ").strip()

def is_score_valid(score):
    return 0 <= score <= 100

def get_valid_scores(prompt, error):
    while True:
        try:
            score = int(input(prompt))
            if is_score_valid(score):
                return score
            print(error)
        except ValueError:
            print("Please Enter a whole number.")

def get_exam_scores(n):
    scores = []
    for i in range(n):
        score = get_valid_scores(
            prompt=f"Exam {i + 1} score: ",
            error="Score must be between 0 and 100. Please Try again."
        )
        scores.append(score)
    return scores

def calc_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def what_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
def what_standing(average):
    if average >= 90:
        return "Dean's List"
    elif average >= 70:
        return "Good Standing"
    elif average >= 60:
        return "Academic Probation"
    else:
        return "Academic Warning"

def print_bars(char = "=", width = 30):
    print (char * width)

def report(name, scores, avg, letter, standing):
    print_bars("=")
    print("STUDENT GRADE REPORT")
    print_bars("=")
    print(f"Student: {name}")
    for i, score in enumerate(scores, 1):
        print(f" Exam {i}: {score}")
    print_bars("-")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {letter}")
    print(f"Standing: {standing}")
    print_bars("=")

def main():
    name = get_student_name()
    scores = get_exam_scores(3)
    avg = calc_average(scores)
    letter = what_letter_grade(avg)
    standing = what_standing(avg)
    report(name, scores, avg, letter, standing)

def test_tracker():
    passed = 0
    failed = 0

    def check(label, result, expected):
        nonlocal passed, failed
        if result == expected:
            print(f" PASS {label}")
            passed += 1
        else:
            print(f" FAIL {label} got {result!r}, expected {expected!r}")
            failed += 1

    print("\n[ is_valid_score ]")
    check("score 0 is valid",   is_score_valid(0),    True)
    check("score 100 is valid", is_score_valid(100),  True)
    check("score 50 is valid",  is_score_valid(50),   True)
    check("score -1 invalid",   is_score_valid(-1),   False)
    check("score 101 invalid",  is_score_valid(101),  False)

    print("\n[ calculate_average ]")
    check("average of [90, 80, 70]",    calc_average([90, 80, 70]),    80.0)
    check("average of [100]",           calc_average([100]),           100.0)
    check("average of [0, 0, 0]",       calc_average([0, 0, 0]),       0.0)
    check("average of empty list",      calc_average([]),              0.0)
    check("average of [92, 85, 78]",    calc_average([92, 85, 78]),    85.0)

    print("\n[ determine_letter_grade ]")
    check("90.0 → A",  what_letter_grade(90.0),  "A")
    check("95.0 → A",  what_letter_grade(95.0),  "A")
    check("89.9 → B",  what_letter_grade(89.9),  "B")
    check("80.0 → B",  what_letter_grade(80.0),  "B")
    check("79.9 → C",  what_letter_grade(79.9),  "C")
    check("70.0 → C",  what_letter_grade(70.0),  "C")
    check("69.9 → D",  what_letter_grade(69.9),  "D")
    check("60.0 → D",  what_letter_grade(60.0),  "D")
    check("59.9 → F",  what_letter_grade(59.9),  "F")
    check("0.0  → F",  what_letter_grade(0.0),   "F")

    print("\n[ determine_standing ]")
    check("90.0 → Dean's List",         what_standing(90.0),  "Dean's List")
    check("70.0 → Good Standing",       what_standing(70.0),  "Good Standing")
    check("85.0 → Good Standing",       what_standing(85.0),  "Good Standing")
    check("60.0 → Academic Probation",  what_standing(60.0),  "Academic Probation")
    check("69.9 → Academic Probation",  what_standing(69.9),  "Academic Probation")
    check("59.9 → Academic Warning",    what_standing(59.9),  "Academic Warning")
    check("0.0  → Academic Warning",    what_standing(0.0),   "Academic Warning")

    print(f"\n{'='*30}")
    print(f"Results: {passed} passed, {failed} failed out of {passed + failed} tests.")
    print('='*30)

test_tracker()
main()