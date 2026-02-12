# problem 1
first = input("Enter First Name: ")
last = input("Enter Last Name: ")
byear = eval(input("Enter Your Birth Year: "))
hobby = input("Enter Your Favorite Hobby:")

first = first.title()
last = last.title()
hobby = hobby.title()

age = 2026 - byear

print("*" * 40)
print(" USER PROFILE CARD".center(40))
print("*" * 40)
print(f"Name: {first} {last}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print("*" * 40)
print("Thanks for making a profile!")

#problem 2

print("*** Text Analyzer ***")

sentence = input("Enter a sentence: ")

spaces = len(sentence)
nospaces = len(sentence.replace(" ", ""))
num_words = len(sentence.split())

vowels = "aeiouAEIOU"
num_vowels = sum(1 for char in sentence if char in vowels)

upper = sentence.upper()
lower = sentence.lower()
reversed = sentence[::-1]

punctuation = ".?!"
capital = "Yes" if sentence[0].isupper() else "No"
ends_punctuation = "Yes" if sentence[-1] in punctuation else "No"

print("*** Analysis Results ***")
print(f"Total characters with spaces: {spaces}")
print(f"Total characters with no spaces: {nospaces}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {num_vowels}")
print(f"Uppercase version: {upper}")
print(f"Lowercase version: {lower}")
print(f"Reversed version: {reversed}")
print(f"Begins with capital: {capital}")
print(f"Ends with puncuation: {ends_punctuation}")
