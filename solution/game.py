"""
    Added board.update(p1,p2)
        Gets all of the pieces in p1 and p2's pieces[]
        Adds them to the board. 

    NEXT:
        Add a way of moving pieces on the board. 

    Would be nice:
        Format Player.print_pieces() to have all coordinates line up
        For Piece.calculate_moves() Have it so that the generated possible_moves[] only includes possible moves and not [-1,-1] to represent illegal moves

    
"""
import chess_resources as chess

Player_W = chess.Player("White")
Player_B = chess.Player("Black")
king = chess.King("White",1,1)
board = chess.Board()
board.update(Player_W,Player_B)
print("Success")


Player_W.print_pieces()
print("")
Player_B.print_pieces()



print(str(Player_B.pieces[2].get_pos_a()),"",str(Player_B.pieces[2].get_pos_b()))

#board.register_players(p1,p2)

"""
    Piece testing
Knight.calculate_moves()
Knight.print_moves()
Knight.change_pos(1,3)

Knight.calculate_moves()
Knight.print_moves()
"""


