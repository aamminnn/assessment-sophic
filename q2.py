# QUESTION 2

"""
  A B C D E
1 - X - X -
2 X - X - X
3 - X - X -
4 X - X - X"
"""

# Creating the square board
# square = []
# rows = [1,2,3,4]
# colum = ['A','B','C','D']
# white = True
# for l in colum:
#     for n in range(1,len(rows)+1):
#         if white == True:
#             square.append(f'{l}'+f'{n}'+'-')
#             white = False
#         else:
#             square.append(f'{l}'+f'{n}'+'X')
#             white = True
# print(square)

# def check_color(sq:list):
#     letter = input("Enter a letter: ").upper()
#     number = input("Enter a number: ")
#     for i in sq:
#         if letter in i and number in i:
#             if 'X' in i:
#                 color = "White"
#             elif '-' in i:
#                 color = "Black"
#             print("The background color is ", color)

# check_color(square)

## 2nd way assuming only read from image
def check_color_2(input_letter, input_number):
    col = ['A','B','C','D','E']
    row = [1,2,3,4]
    for l in col:
        if l == 'B' or l == 'D':
            initial_white = False # check initial color in every column
        else:
            initial_white = True #check intial color in every column
        if l == input_letter:
            for n in row:
                if initial_white == True:
                    i = n % 2 
                    if i == 0:
                        white_square = False # alternate between black and white based on initial color
                    else:
                        white_square = True # alternate between black and white based on initial color
                else:
                    i = n % 2 
                    if i == 0:
                        white_square = True # alternate between black and white based on initial color
                    else:
                        white_square = False # alternate between black and white based on initial color
                if n == int(input_number):
                    if white_square == True:
                        square_color = 'White' # color at specific index
                    else:
                        square_color = 'Black' # color at specific index
            break
    return square_color
    
input_letter = input("Enter a letter: ").upper()
input_number = input("Enter a number: ")
color = check_color_2(input_letter, input_number)
print("The background color is ", color)

