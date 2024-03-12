#1
# def apply_operation(num1, num2, operation):
#     if operation == "+":
#         print(num1 + num2)
#     elif operation == "-":
#         print(num1 - num2)
#     elif operation == "*":
#         print(num1 * num2)
#     elif operation == "/":
#         if num2 == 0:
#             print("Error: Division by zero")
#         else:
#             print(num1/num2)
#     else:
#         print("Operation is not valid")  

# apply_operation(2, 0, '/')   




#2
# def triangle_area(height, width):
#         print(height * width / 2)


# def rectangle_area(length, width):
#         print(length * width)


# def trapezium_area(length1, length2, height):
#         print((length1 + length2) * height / 2)


# def choose_shape():
#         print("choose a shape:")
#         print("triangle")
#         print("rectangle")
#         print("trapezium")

#         user_choice = input("enter your choice: ")

#         if user_choice == "triangle":
#                 height = int(input("enter triangle's height: "))
#                 width = int(input("enter triangle's wdith: "))
#                 triangle_area(height, width)
#         elif user_choice == "rectangle":
#                 length = int(input("enter rectangle's length: "))
#                 width = int(input("enter rectangle's wdith: "))
#                 rectangle_area(length, width)
#         elif user_choice == "trapezium":
#                 length1 = int(input("enter trapezium's first base length: "))
#                 length2 = int(input("enter trapezium's second base length: "))
#                 height = int(input("enter trapezium's height: "))
#                 trapezium_area(length1, length2, height)
#         else:
#             print("invlaid input")
            
# choose_shape()


#3

# board = [' ', ' ', ' ',
#         ' ', ' ', ' ',
#         ' ', ' ', ' ']
# currentPlayer = "X"
# winner = None
# gameRunning = True

# #დაფის დაპრინტვა
# def PrintBoard(board):
#     print(board[0] + " | " + board[1] + " | " + board[2])
#     print("---------")
#     print(board[3] + " | " + board[4] + " | " + board[5])
#     print("---------")
#     print(board[6] + " | " + board[7] + " | " + board[8])

# #მოთამაშეს შემოჰყავს ინპუტი
# def PlayerInput(board):
#     inp = int(input("Enter a number from 1-9: "))
#     if inp >= 1 and inp <= 9 and board[inp-1] == " ":
#         board[inp-1] = currentPlayer
#     else:
#         print("sapce is not empty")

# #შემოწმება ჰორიზონტალურად
# def horizontal_check(board):
#     global winner
#     if board[0] == board[1] == board[2] and board[0] != " ":
#         winner = board[0]
#         return True
#     elif board[3] == board[4] == board[5] and board[3] != " ":
#         winner = board[3]
#         return True
#     elif board[6] == board [7] == board[8] and board[6] != " ":
#         winner = board[6]
#         return True
    
# #შემოწმება ვერტიკალურად
# def vertical_check(board):
#     global winner
#     if board[0] == board[3] == board[6] and board[0] != " ":
#         winner = board[0]
#         return True
#     elif board[1] == board[4] == board[7] and board[1] != " ":
#         winner = board[1]
#         return True
#     elif board[2] == board [5] == board[8] and board[2] != " ":
#         winner = board[2]
#         return True

# #შემოწმება დიაგონალურად
# def diagonal_check(board):
#     global winner
#     if board[0] == board[4] == board[8] and board[0] != " ":
#         winner = board[0]
#         return True
#     elif board[2] == board[4] == board[6] and board[2] != " ":
#         winner = board[2]
#         return True
    
# #ფრეს დამთავრების შემთხვევა
# def tie_check(board):
#     global gameRunning
#     if " " not in board:
#         print(board)
#         print("Tie")
#         gameRunning = False


# #მოგების შემოწმება
# def  winner_chek():
#     if horizontal_check(board) or diagonal_check(board) or vertical_check(board) == True:
#         print(f"Winner is {winner}")
        

# #მოთამშეებს შორის შეცვლა
# def switchPlayer():
#     global currentPlayer
#     if currentPlayer == "X":
#         currentPlayer = "O"
#     else:
#         currentPlayer = "X"



# while gameRunning:
#     PrintBoard(board)
#     PlayerInput(board)
#     winner_chek()
#     tie_check(board)
#     switchPlayer()