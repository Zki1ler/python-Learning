##1
principle = float(input("Principle: "))
rate = float(input("Rate (%): "))
time = float(input("Time: "))

balence = principle 
for time in range(1, int(time) + 1):
    balence = balence * (1 + rate / 100)
    print(f"Year {time}: Balence = {balence:.2f}") 
    
total_interest = balence - principle
print(f"Total interest earned: {total_interest:.2f}")

##2

def caesar_encode(text, shift):
    results = ""
    for cha in text:
        if cha.isalpha():
            if cha.islower():
                results += chr((ord(cha) - 97 + shift) % 26 + 97)
            else:
                results += chr((ord(cha) - 65 + shift) % 26 + 65)
        else:
            results += cha
    return results

print(caesar_encode("Hello, World!", 3))
print(caesar_encode("abc xyz", 2))
print(caesar_encode("Python 3", 5))

##3
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result
m1 = [[1, 2, 3], 
      [4, 5, 6]]

m2 = [[1, 2], 
      [3, 4], 
      [5, 6]]

print(transpose(m1))
print(transpose(m2))


##4
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    for row in board:
        if " " in row:
            return "Ongoing"
    return "Draw"




board1 = [["X", "X", "X"],
["O", "O", " "],
[" ", " ", " "]]
print(check_winner(board1)) # X

board2 = [["X", "O", "X"],
["X", "O", " "],
[" ", "O", "X"]]

print(check_winner(board2)) # O

board3 = [["X", "O", "X"],
["X", "O", "O"],
["O", "X", "X"]]
print(check_winner(board3)) # Draw
board4 = [["X", "O", " "],
[" ", "X", " "],
[" ", " ", " "]]
print(check_winner(board4)) # Ongoing
