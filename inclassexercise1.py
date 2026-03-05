name = "Taylor"
age = 21
course = "Computer Science"  # 'class' is a keyword
score = 100

print(name, age, course, score)

a = 256
b = 256
print("a =", a, "id(a) =", id(a))
print("b =", b, "id(b) =", id(b))
print("Same object?", id(a) == id(b))

print()

c = 257
d = 257
print("c =", {c}, "id(c) =", {id(c)})
print("d =", {d}, "id(d) =", {id(d)})
print("Same object?", {id(c) == id(d)})

email="johnsmith@email.com"
age =2026-2004
Adult= age>=18
message ="Welcome" if Adult else "Sorry, too young"
print(message)

##I think that the reason variables are labels not containers is because each has there own specific thing about them while containers have multiple things about them. For example a string doesn't encompass anything that an integer has and vise versa while if they were containers there would be multiple things that probably over lapped about them.
