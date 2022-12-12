"""
12/12 
        BUGS >@<
            Github Issue #4: King being shown as in check when an enemy move takes him out of check
    

        Overall changes:
            Added Pawn Promotion:
                Pawns get promoted into a different piece when they make it to the top.
                Anything other than Pawn or King

            Fixed Github issue #2 If an attempted move is made on a piece that has fallen, a fatal error is thrown
            
            
        Board:
            Added is_valid_promotion()
            Fixed puts_enemy_in_check()

        Pieces:
            Added pieces_promoted = {}
            Added add_piece()
            Added promote_pawn()
            Added get_piece_names()
            Added is_legal_pos()
            Added get_instances()
            Added get_live_names()

        Player:

    NEXT:
            



            Add castling:
                ---
                The king and the Rook move towards eachother and swap places.
                In order to do this, move your ing not one, but two spaces towards the rook you are castling with
                Then place the Rook on the opposite side of the King. 
                ---
                Prerequisites:
                    - The King and rook may not have moved,
                    - There must not be any obstruction between the pieces
                    - The King cannot move through Check 
            
            Add En Passant:
                ---
                A pawn moving forward two squares on the first turn can be captured "En passant" by an enemy pawn
                If and only if it has moved two spaces (First turn)
                And it lands next to the enemy Pawn. 
                The capturing pawn takes the moving Pawn by attacking the square behind the moving pawn. 
                ---

            Add check mate condition

    Would be nice:
        Add board.move_counter() functionality
        Add a dictionary to track moves and events 
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

game.register_move("White", "Pawn_3",      4,2)
game.register_move("White", "Pawn_3",      3,2)
game.register_move("White", "Pawn_3",      2,2)

game.register_move("White", "Knight_1",    5,2)
game.register_move("White", "Knight_1",    3,1)
game.register_move("White", "Knight_1",    1,2)

game.register_move("White", "Knight_1",    2,0)
game.register_move("Black", "Pawn_4",      2,3)
game.register_move("Black", "Bishop_1",    2,4)

game.register_move("White", "Pawn_3",      1,2)
game.register_move("White", "Pawn_3",      0,2)









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


