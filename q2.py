# QUESTION 2

"""
  A B C D E
1 - X - X -
2 X - X - X
3 - X - X -
4 X - X - X"
"""

# Creating the square board
square = []
rows = [1,2,3,4]
colum = ['A','B','C','D']
white = True
for l in colum:
    for n in range(1,len(rows)+1):
        if white == True:
            square.append(f'{l}'+f'{n}'+'-')
            white = False
        else:
            square.append(f'{l}'+f'{n}'+'X')
            white = True
print(square)

def check_color(sq:list):
    letter = input("Enter a letter: ").upper()
    number = input("Enter a number: ")
    for i in sq:
        if letter in i and number in i:
            if 'X' in i:
                color = "White"
            elif '-' in i:
                color = "Black"
            print("The background color is ", color)

check_color(square)