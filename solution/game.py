"""
15/12 
        BUGS >@<
            Github Issue #4: King being shown as in check when an enemy move takes him out of check
    

        Overall changes:
            Added Castling. 
            
            
        Board:
            Added is_legal_castle()
            Added castle()
            Moved the functions around

        Pieces:           
            Added first_turn to all pieces
            Added first_turn_complete()
            Added Castling movements to King's moveset

        Player:
            Added the full piece names to valid_names tuple
            Added is_legal_name()


    NEXT:   
            Test castling:
                    King's moveset is removed after the first turn and he can't move left and right two.
                    All instances of castling    

            Investigate:
            Github Issue 4: King being shown as in check when an enemy move takes him out of check
            Github Issue 5: Pawn reaching otherside dialogue being triggered when it shouldn't

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

game.register_move("White", "Pawn_4",      5,3)
game.register_move("White", "Bishop_1",    5,4)
game.register_move("White", "Queen",       6,3)
game.register_move("White", "Knight_1",    5,0)
game.register_move("White", "King",        7,2)





print("")
game.p1.print_pieces()
print("")
game.p2.print_pieces()
