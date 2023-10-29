# inputs
# AI IS ALWAYS 1, player 1.

inputs = {                                                         #   big     small
"previous_moves" : {}, # previous moves going from oldest to newest "<1 or 2>":[row,col, row, col]
"board_settings" : [ # 0 is none, 1 is player o, 2 is player x
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

outputs={
    "next_move": [] #[row, col, row, col]
}