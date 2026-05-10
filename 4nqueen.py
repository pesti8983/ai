# Simple N-Queen Program in Python

N = 4

# Check if queen can be placed
def is_safe(board, row, col):

    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# Solve using backtracking
def solve(board, col):

    # All queens placed
    if col == N:
        return True

    for row in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main program
board = [[0] * N for i in range(N)]

if solve(board, 0):

    print("Solution:")

    for row in board:
        print(row)

else:
    print("No Solution")