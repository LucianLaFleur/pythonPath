import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def create_board():
  # 6 rows and 7 columns for making the board
  board = np.zeros((ROW_COUNT, COL_COUNT))
  return board

def drop_piece(board, row, col, piece):
  board[row][col] = piece

def is_valid_location(board, col):
  return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
  for r in range(ROW_COUNT):
    if board[r][col] == 0:
      return r

# flip the board to fill bottom up
def print_board(board):
  # flip board over x axis
  print(np.flip(board, 0))

# ceck for a winning condition
def winning_move():
  # check horizontal positions that could make a 4-set
  for c in range(COL_COUNT-3):
    for r in range(ROW_COUNT):
      # iterate to clean this up in a for loop
      if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
        return True
  # check columnal wins
  for c in range(COL_COUNT):
    for r in range(ROW_COUNT-3):
      # iterate to clean this up in a for loop
      if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        return True
  # check ltr sloped (positive) diagonals
  for c in range(COL_COUNT-3):
    for r in range(ROW_COUNT-3):
      # iterate to clean this up in a for loop
      if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        return True
  # check rtl sloped (negative) diagonals
  for c in range(COL_COUNT-3):
    #  !!! Note: start param is 3 because idx 3 up is the first possible start for a 4 downward diagonal.
    for r in range(3, ROW_COUNT):
      # iterate to clean this up in a for loop
      if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
        return True



board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
  # get player1's turn
  if turn == 0:
    # make validation for selection
    col = int(input("Player 1's turn... (type 0-6): "))
    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col 1)

      if winning_move(board, 1)
        print("Player 1 victory")
  else:
    col = int(input("Player 2's turn~~~ (type 0-6)"))
 
    if is_valid_location(board, col):
      row = get_next_open_row(board, col)
      drop_piece(board, row, col 1)

  print_board(board)
  # alternate turns by using modulo for even/odd
  turn +=1
  turn = turn % 2