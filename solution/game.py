"""
19/12 
        BUGS >@<
           
    

        Overall changes:
            Added En Passant. Needs testing       
            
            
        Board:
            Added calculate_passant()
            Added close_passant()


        Pieces:           
            (PawnW & PawnB) 
                Added passant_victim_pos
                Added can_passant()
                Added can_not_passant()

        Player:



    NEXT:
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


game.register_move("White", "Pawn_5", 4,4)
game.register_move("White", "Pawn_5", 3,4)
game.register_move("Black", "Pawn_4", 3,3)
game.register_move("White", "Pawn_5", 2,3)








#game.register_move("White", "King", 7,2)
#game.register_move("Black", "King", 0,6)




print("")
game.p1.print_pieces()
print("")
game.p2.print_pieces()


