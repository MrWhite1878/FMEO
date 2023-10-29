import Main

#AI is player 1 (O)

# inputs
inputs = {
"previous_moves" : {}, # previous moves going from oldest to newest "<1 or 2>":[row,col, row, col]
"board_settings" : [   # 0 is none, 1 is player o, 2 is player x
    [[[[0, 0, 0], 
       [0, 0, 0], 
       [0, 0, 0]], [[0, 0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0]], [[0, 0, 0], 
                                 [0, 0, 0], 
                                 [0, 0, 0]]],
     [[[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]], [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]], [[0, 0, 0],
                                 [0, 0, 0],
                                 [0, 0, 0]]],
     [[[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]], [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]], [[0, 0, 0],
                                 [0, 0, 0],
                                 [0, 0, 0]]]]
]}

# identify possible moves
def possible_moves():
  return
# look into the future
def look_ahead(depth):
  return

# evaluate the board
def evaluate():
  return

# minimax algorithm
def minimax():
  return

# alpha beta pruning
def alpha_beta():
  return

# make a move
def make_move():
  return


# outputs
outputs={
    "next_move": [] #[row, col, row, col]
}