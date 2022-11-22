"""
    Added all pieces 
    Added their move matrices 
    Added the Calculate Postion function
    Added a print_moves() function to show moves
    Added a pieces[] to <Player> 
    Added an __init__ to <Player>
    Added Player.print_pieces()

    NEXT:
        Add a matrix of pieces to the Board class
        Add a List of pieces to the player classs

    Would be nice:
        Format Player.print_pieces() to have all coordinates line up
        For Piece.calculate_moves() Have it so that the generated possible_moves[] only includes possible moves and not [-1,-1] to represent illegal moves
    
"""
import chess_resources as chess

Player_W = chess.Player("White")
Player_B = chess.Player("Black")

print("Success")

z = chess.Board

Player_W.print_pieces()
print("")
Player_B.print_pieces()

"""
    Piece testing
Knight.calculate_moves()
Knight.print_moves()
Knight.change_pos(1,3)

Knight.calculate_moves()
Knight.print_moves()
"""


