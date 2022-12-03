"""
    03/12 
        Overall changes:         
        Pawns can now only take diagonally and when space is occupied by enemy
        Pawns can't march when space is occupied       
        Units can't ghost through other units, Queen, rook, bishop
        Added "Illegal move: Path blocked" error messages for Queen, Bishop and Rook
        Added "Illegal move: Space occupied by friendly" Error message
        Added "Illegal move: Pawn can't attack forwards. 

            
        Board:
            Added path_is_blocked()
            Added get_space()
            
        Pieces:
            Added is_in_moveset()

        Player:
            Added pieces_taken{}

    NEXT:
            Make sure all pieces move accordingly,                 
                (King doesn't put himself in danger)
            Implement type catchers on is_legal_move()
                Pawn Done
                Bishop Done
                Rook
                Queen
                King 

            Add taking of pieces         
            Pawns turn into a different piece when they make it to the top. 
            Add score keeping 
            Add check condition
            Add check mate condition

    Would be nice:
        Format Player.print_pieces() to have all coordinates line up        
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
board.register_move(Player_W.pieces["pawn_5"], 5,4)
board.register_move(Player_B.pieces["pawn_2"], 2,1)
board.register_move(Player_W.pieces["pawn_5"], 4,4)
board.register_move(Player_B.pieces["pawn_2"], 3,1)
board.register_move(Player_W.pieces["bishop_2"], 2,0)

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


