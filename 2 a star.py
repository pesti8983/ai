import heapq
from termcolor import colored


# ------------------------------------------
# Class to represent Puzzle State
# ------------------------------------------
class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


# ------------------------------------------
# Display Puzzle Board
# ------------------------------------------
def print_board(board):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        row = "|"
        for tile in board[i:i+3]:
            if tile == 0:
                row += f" {colored(' ', 'cyan')} |"
            else:
                row += f" {colored(str(tile), 'yellow')} |"
        print(row)
        print("+---+---+---+")


# ------------------------------------------
# Goal State
# ------------------------------------------
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]


# ------------------------------------------
# Possible Moves
# ------------------------------------------
moves = {
    'U': -3,
    'D': 3,
    'L': -1,
    'R': 1
}


# ------------------------------------------
# Heuristic Function (Manhattan Distance)
# ------------------------------------------
def heuristic(board):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(board[i] - 1, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# ------------------------------------------
# Move Tile Function
# ------------------------------------------
def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_pos = blank_pos + moves[move]

    new_board[blank_pos], new_board[new_pos] = \
        new_board[new_pos], new_board[blank_pos]

    return new_board


# ------------------------------------------
# A* Algorithm
# ------------------------------------------
def a_star(start_state):
    open_list = []
    closed_set = set()

    start = PuzzleState(start_state, None, None, 0,
                        heuristic(start_state))
    heapq.heappush(open_list, start)

    while open_list:
        current = heapq.heappop(open_list)

        if current.board == goal_state:
            return current

        closed_set.add(tuple(current.board))
        blank_pos = current.board.index(0)

        for move in moves:
            # Skip invalid moves
            if move == 'U' and blank_pos < 3:
                continue
            if move == 'D' and blank_pos > 5:
                continue
            if move == 'L' and blank_pos % 3 == 0:
                continue
            if move == 'R' and blank_pos % 3 == 2:
                continue

            new_board = move_tile(current.board, move, blank_pos)

            if tuple(new_board) in closed_set:
                continue

            new_state = PuzzleState(
                new_board,
                current,
                move,
                current.depth + 1,
                current.depth + 1 + heuristic(new_board)
            )

            heapq.heappush(open_list, new_state)

    return None


# ------------------------------------------
# Print Solution Path
# ------------------------------------------
def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent

    path.reverse()

    for step in path:
        print(f"\nMove: {step.move}")
        print_board(step.board)


# ------------------------------------------
# Main Execution
# ------------------------------------------
if __name__ == "__main__":

    initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]

    solution = a_star(initial_state)

    if solution:
        print(colored("Solution found!", "green"))
        print_solution(solution)
    else:
        print(colored("No solution exists.", "red")) 