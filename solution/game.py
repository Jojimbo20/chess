"""
    01/12 
        Overall changes: 
            Added a print funtion to each class module for checking of successful access.
            The board can now register moves and disallows the movement if the move is out of bounds or occupied by friendly.
            
        Board:
            Added __init__(self, p1,p2) It's easier for reading if the board has player references
            Added update(self) Resets the board to zero, re-populates matrix with pieces current positions. 
            Added register_move(self, _piece, _pos_a, _pos_b)
            Added is_legal_move(self, _piece, _pos_a, _pos_b):
            Added calculate_moves(self, _piece):
            
        Pieces:
            Added get functions; name, colour
            Added possible moves[] to the parent class
            Moved calculate_moves() to board class for access to all pieces positions in the game
    NEXT:
            Make sure all pieces move accordingly, 
                (King doesn't put himself in danger) 
                (Pawns only take diagonally)
                (Units can't ghost through other units)(Queen, rook, bishop)
            Add taking of pieces            
            Add score keeping 
            Add check condition
            Add check mate condition


    Would be nice:
        Format Player.print_pieces() to have all coordinates line up
        For Piece.calculate_moves() Have it so that the generated possible_moves[] only includes possible moves and not [-1,-1] to represent illegal moves
        Represent pieces in a nice printed way. 
        Type commands into command line
"""
import chess_resources as chess

Player_W = chess.Player("White")
Player_B = chess.Player("Black")
board = chess.Board(Player_W, Player_B)

print("game.py started successfully")
"""
    Player.pieces{}
    king
    queen   
    bishop_1/2
    knight_1/2
    rook_1/2 
    pawn_1-8
"""


Player_W.print_pieces()
print("")
#Player_W.move_piece("king",3,3)
board.update()
board.register_move(Player_W.pieces["king"], -1,3)




Player_W.print_pieces()
print("")
Player_B.print_pieces()


#board.register_players(p1,p2)

"""
    Piece testing
Knight.calculate_moves()
Knight.print_moves()
Knight.change_pos(1,3)

Knight.calculate_moves()
Knight.print_moves()
"""


