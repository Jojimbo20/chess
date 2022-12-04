"""
    04/12 
        Overall changes:         
        Attacking and taking of pieces now works as it should
        Added a way of checking a players score (Total of taken pieces)
            
        Board:
            Added attack_square()
            Added an is_alive() check to is_legal_move()
            
        Pieces:
            moved name variable into  __init__()
            Added kill(self)
            Added is_alive()

        Player:
            Added get_colour()
            Added self.score
            Added get_score()
            Added kill_piece()
            Added take_piece()
            Changed the naning properties of the pieces so that passing of names is easier and displaying of names is more specific. 

    NEXT:
            Make sure all pieces move accordingly,                 
                (King doesn't put himself in danger)
            Implement type catchers on is_legal_move()
                Pawn Done
                Bishop Done
                Rook
                Queen
                King 

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
board.register_move(Player_W.pieces["Pawn_5"], 5,4)
board.register_move(Player_B.pieces["Pawn_2"], 2,1)
board.register_move(Player_W.pieces["Pawn_5"], 4,4)
board.register_move(Player_B.pieces["Pawn_2"], 3,1)
board.register_move(Player_W.pieces["Bishop_2"], 3,1)

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


