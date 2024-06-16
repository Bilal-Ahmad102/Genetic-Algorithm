import random

def generateRandomState(rows=6, columns=7):
    total_cells = rows * columns
    half_cells = total_cells // 2
    
    # Create a list with equal numbers of 'x' and 'o'
    cells = ['x'] * half_cells + ['o'] * half_cells
    
    # If total_cells is odd, we add one more 'x' or 'o'
    if total_cells % 2 != 0:
        cells.append('x')  # or 'o', just to balance
    
    # Shuffle the list to randomize the positions
    random.shuffle(cells)
    
    return cells

def printState(board, rows=6, columns=7):
    for i in range(rows-1, -1, -1):
        print("\t", end="")
        for j in range(columns):
            print("| " + str(board[i * columns + j]), end=" ")
        print("|")
    print("\t  _   _   _   _   _   _   _ ")
    print("\t  1   2   3   4   5   6   7 ")

# test = []
# for i in range(6*7):
#     if i%2==0: test.append('x')
#     else:test.append('o')
    
# # Generate a random initial board state
# initial_board = generateRandomState()
# print(test)
# # Print the current game state
# printState(test)