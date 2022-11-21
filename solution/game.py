import chess_resources as chess

Knight = chess.Knight("Knight","White", 7, 1)
y = chess.Player
z = chess.Board
Knight.calculate_moves()
Knight.print_moves()
Knight.change_pos(1,3)

Knight.calculate_moves()
Knight.print_moves()

"""
    Added all pieces 
    Added their move matrices 
    Added the Calculate Postion function
    Added a print_moves() function to show moves

    NEXT:
        Add a matrix of pieces to the Board class
        Add a List of pieces to the player classs
    
"""

