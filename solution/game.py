"""
    10/12 
        BUGS >@<
            ATTEMPTING TO MOVE A FALLEN PIECE
            If an attempted move is made on a piece that has fallen, an error is thrown
                The cause of this is to do with how pieces are taken, 
                First they're added into player1.pieces_taken{}
                The piece is then deleted from player2.pieces{}
                So when 
                board.register_move(Player_B.pieces["FALLEN_PIECE"], pos_a, pos_b)            
                Is called, it's actually referencing a key pair that doesn't exist within the dictionary. 
                The fix will have to be implemented later on when I implement a way of interacting with the board Library
                With a catch to throw the error that the piece isn't alive before passing it to that functions

                King throwing Illegal move:  Puts self in check error when it's a legal move
                Something to do with Bishop returning path clear in puts_king_in_check()
    

        Overall changes:
            
            
        Board:
            __init__() no longer requires player references
            Added valid_names tuple
            Added a Move counter (Yet to implement fucntionality)
            Added is_valid_name()
            Changed register_move() funcitonality
                Is now used as such register_move(player, piece, pos_a, pos_b) where 'player' and 'piece' are string references
            Fixed some King check bugs
            Cleaned up is_legal_move() for readability and removed redundant code

            
            
        Pieces:

        Player:

    NEXT:
            Fix King throwing Illegal move bug
            Pawns turn into a different piece when they make it to the top.
            Add check mate condition

    Would be nice:
        Add board.move_counter() functionality
        Format Player.print_pieces() to have all coordinates line up        
        Represent pieces in a nice printed way. 
        Type commands into command line
"""
import chess_resources as chess

game = chess.Board()

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


game.p1.print_pieces()
print("")
game.update()

game.register_move("White", "Pawn_2",      5,1)
game.register_move("Black", "Pawn_3",      3,2)
game.register_move("White", "Bishop_1",    5,0)
game.register_move("Black", "King",        1,2)
game.register_move("White", "Pawn_6",      5,5)
game.register_move("Black", "King",        2,3)
game.register_move("White", "Pawn_6",      4,5)
game.register_move("Black", "Pawn_3",      4,2)
game.register_move("Black", "King",        2,4)
game.register_move("White", "Pawn_6",      3,5)




print("")
game.p1.print_pieces()
print("")
game.p2.print_pieces()


"""
Piece testing
Knight.calculate_moves()
Knight.print_moves()
Knight.change_pos(1,3)
Knight.calculate_moves()
Knight.print_moves()
"""


