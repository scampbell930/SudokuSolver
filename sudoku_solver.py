# Initializing sudoku board with 23 clues (anything smaller takes much longer to calculate)
sudoku_board = [
    [" ", " ", " ", 6, " ", " ", 4, " ", " "],
    [7, " ", " ", " ", " ", 3, 6, " ", " "],
    [" ", " ", " ", " ", 9, 1, " ", 8, " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", 5, " ", 1, 8, " ", " ", " ", 3],
    [" ", " ", " ", 3, " ", 6, " ", 4, 5],
    [" ", 4, " ", 2, " ", " ", " ", 6, " "],
    [9, " ", 3, " ", " ", " ", " ", " ", " "],
    [" ", 2, " ", " ", " ", " ", 1, " ", " "]
]


# Function print_board is a void function that prints out an input sudoku board
def print_board(board):
    # Loop through board columns
    for i in range(len(board)):
        # Check if loop is at the end of horizontal section
        if i != 0 and i % 3 == 0:
            print("- - - - - - - - - - - - -")

        # Loop through board rows
        for j in range(len(board[0])):
            # Check if loop is at the end of vertical section
            if j != 0 and j % 3 == 0:
                print(" | ", end="")

            # Print value
            # Check if loop is at end of row
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Function is_empty returns the location if it currently has no value
def is_empty(board):
    # Loop through board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Check if location is empty
            if board[i][j] == " ":
                # Return the location on the board in (row, column)
                return i, j

    # Board has no empty locations
    return None


# Function is_valid determines if a value is legal in its current location
def is_valid(board, value, location):
    # Check column
    for i in range(len(board)):
        # Check if value is already in column
        if board[i][location[1]] == value and location[0] != i:
            return False

    # Check row
    for j in range(len(board[0])):
        # Check if value is already in row
        if board[location[0]][j] == value and location[1] != j:
            return False

    # Check 3x3
    # Determine which square value is located in
    square_x = location[1] // 3
    square_y = location[0] // 3

    # Loop through current square
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            # Check if value is already in square
            if board[i][j] == value and (i, j) != location:
                return False

    return True


# Function solve is a recursive algorithm that calculates the answer to the sudoku board
def solve(board):
    # Initialize empty space
    empty = is_empty(board)
    # Base case checks if board is full
    if not empty:
        return True
    else:
        # Initialize location of empty space
        row, column = empty

    # Loop through possible values
    for i in range(1, 10):
        # Check if i is a legal value
        if is_valid(board, i, (row, column)):
            # Add value to board
            board[row][column] = i

            # Check if board has been solved
            if solve(board):
                return True

            # Backtrack as solution was invalid
            board[row][column] = " "

    return False


print("Input Board:")
print_board(sudoku_board)
solve(sudoku_board)
print()
print("---------------------------")
print()
print("Solved Board:")
print_board(sudoku_board)
