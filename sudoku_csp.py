# Sudoku Solver using CSP (Backtracking)

N = 9

# Sample Sudoku (0 = empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print board
def print_board(board):
    for row in board:
        print(row)

# Find empty cell
def find_empty(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j
    return None

# Check if valid
def is_valid(board, row, col, num):
    # Row check
    if num in board[row]:
        return False

    # Column check
    for i in range(N):
        if board[i][col] == num:
            return False

    # 3x3 grid check
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Backtracking solver
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Run
if solve(board):
    print("Solved Sudoku:\n")
    print_board(board)
else:
    print("No solution exists")
