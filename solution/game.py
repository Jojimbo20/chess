"""
    08/12 
        BUGS >@<
            ATTEMPTING TO MOVE A FALLEN PIECE
            If an attempted move is made on a piece that has fallen, an error is thrown
                The cause of this is to do with how pieces are taken, 
                First they're added into player1.pieces_taken{}
                The piece is then deleted from player2.pieces{}
                So when 
                board.register_move(Player_B.pieces["FALLEN_PIECE"], pos_a, pos_b)            
                Is called, it's actually referencing a key pair that doesn't exist within the dictionary. 

                The fix will have to be implemented later on when I implement a way of user input, 
                With a catch to throw the error that the piece isn't alive before passing it to that function
    

        Overall changes:
        Pawns can now move two spaces forward on the first go (BUGGY)
        King can't put himself in danger 
        Added check condition
        Fixed the Pawn not being able to move two spaces on first go after one pawn has moved. 
            
        Board:
            Added check_enemy()
            Added uncheck_self()
            Added puts_enemy_king_in_check()
            Added puts_king_in_check()
            
            
        Pieces:
            Added first move conditions to Pawn_W and Pawn_B

        Player:

    NEXT:
            Pawns can move 2 forward on first turn (Half implemented - see bugs)
            Pawns turn into a different piece when they make it to the top. 
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
print("")
"""
    Player.pieces{}
    King
    Queen   
    Bishop_1/2
    Knight_1/2
    Rook_1/2 
    Pawn_1-8
"""


Player_W.print_pieces()
print("")
board.update()

board.register_move(Player_W, Player_W.pieces["Pawn_4"], 4,3)
board.register_move(Player_B, Player_B.pieces["Pawn_4"], 3,3)

board.register_move(Player_B, Player_B.pieces["King"], 1,3)
board.register_move(Player_B, Player_B.pieces["King"], 2,3)
board.register_move(Player_B, Player_B.pieces["King"], 3,4)
board.register_move(Player_W, Player_W.pieces["Pawn_5"], 4,4)
board.register_move(Player_W, Player_W.pieces["Pawn_5"], 3,4)









print("")
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


