"""
16/12 
        BUGS >@<
           
    

        Overall changes:
            Fixed Github Issue 5: Pawn reaching otherside dialogue being triggered when it shouldn't
            Fixed Github Issue 4: King being shown as in check when an enemy move takes him out of check
            Tested castling, all working as it should         
            
            
        Board:
            Added uncheck_enemy()


        Pieces:           
            Changed some of King's attributes so that each instance has their own Moveset. 

        Player:



    NEXT:
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

def move_pawns_forward(_player, _spaces, _game):

    if "White" in _player:
        for piece in _game.p1.pieces.values():
            if "Pawn" not in piece.get_name():
                continue
            _game.register_move("White", piece.get_name(),      (piece.get_pos_a() - _spaces), piece.get_pos_b())
    else:
        for piece in _game.p2.pieces.values():
            if "Pawn" not in piece.get_name():
                continue
            _game.register_move("Black", piece.get_name(),      (piece.get_pos_a() + _spaces), piece.get_pos_b())

def kill_pawns(_game):
    pawns = []
    for pawn in _game.p1.pieces.values():
        if "Pawn" not in pawn.get_name():
            continue
        pawns.append(pawn)
    for pawn in pawns:
        _game.p1.kill_piece(pawn)

    pawns = []

    for pawn in _game.p2.pieces.values():
        if "Pawn" not in pawn.get_name():
            continue
        pawns.append(pawn)

    for pawn in pawns:
        _game.p2.kill_piece(pawn)
    


def check_castling(_game):
    move_pawns_forward("White", 2, _game)
    move_pawns_forward("Black", 2, _game)
    _game.register_move("White", "Queen", 6,3)
    _game.register_move("Black", "Queen", 1,3)
    _game.register_move("White", "Bishop_1", 6,1)
    _game.register_move("White", "Bishop_2", 6,6)
    _game.register_move("Black", "Bishop_1", 1,1)
    _game.register_move("Black", "Bishop_2", 1,6)
    _game.register_move("Black", "Knight_1", 2,0)
    _game.register_move("Black", "Knight_2", 2,7)
    _game.register_move("White", "Knight_1", 5,0)
    _game.register_move("White", "Knight_2", 5,7)
    """
        UNCOMMENT AS NEEDED
    """

    #Queen side castling
    #_game.register_move("White", "King", 7,2)
    #_game.register_move("Black", "King", 0,2)
    
    #King side castling
    #_game.register_move("White", "King", 7,6)
    #_game.register_move("Black", "King", 0,6)

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



kill_pawns(game)
game.register_move("White", "Queen", 6,3)
game.register_move("Black", "Queen", 1,3)
game.register_move("White", "Bishop_1", 6,1)
game.register_move("White", "Bishop_2", 6,6)
game.register_move("Black", "Bishop_1", 1,1)
game.register_move("Black", "Bishop_2", 1,6)
game.register_move("Black", "Knight_1", 2,0)
game.register_move("Black", "Knight_2", 2,7)
game.register_move("White", "Knight_1", 5,0)
game.register_move("White", "Knight_2", 5,7)
#King can't be in check
#King can't move through check
#King can't land in check

game.register_move("White", "Knight_1", 3,1)
game.register_move("White", "Knight_1", 2,3)
game.register_move("White", "Knight_1", 4,4)






#game.register_move("White", "King", 7,2)
#game.register_move("Black", "King", 0,6)




print("")
game.p1.print_pieces()
print("")
game.p2.print_pieces()


