import chess_resources as chess
print("Player.py accessed")

class Player(object):
    #The number of Pieces 
    score = 0

    def __init__(self, _colour):  
        self.colour = _colour
        self.pieces = {}
        self.pieces_taken = {}

        if _colour != "White" and _colour != "Black":
            print("ERROR: Colour must be 'White' or 'Black'")
        elif _colour == "White":
            king    = chess.King(_colour,   7, 3,"King")
            queen   = chess.Queen(_colour,  7, 4,"Queen")             
            bishop_1= chess.Bishop(_colour, 7, 2,"Bishop_1")
            bishop_2= chess.Bishop(_colour, 7, 5,"Bishop_2")
            knight_1= chess.Knight(_colour, 7, 1,"Knight_1")
            knight_2= chess.Knight(_colour, 7, 6,"Knight_2")
            rook_1  = chess.Rook(_colour,   7, 0,"Rook_1")
            rook_2  = chess.Rook(_colour,   7, 7,"Rook_2")
            pawn_1  = chess.Pawn_W(_colour, 6, 0,"Pawn_1")
            pawn_2  = chess.Pawn_W(_colour, 6, 1,"Pawn_2")
            pawn_3  = chess.Pawn_W(_colour, 6, 2,"Pawn_3")
            pawn_4  = chess.Pawn_W(_colour, 6, 3,"Pawn_4")
            pawn_5  = chess.Pawn_W(_colour, 6, 4,"Pawn_5")
            pawn_6  = chess.Pawn_W(_colour, 6, 5,"Pawn_6")
            pawn_7  = chess.Pawn_W(_colour, 6, 6,"Pawn_7")
            pawn_8  = chess.Pawn_W(_colour, 6, 7,"Pawn_8")

            
            self.pieces['King'    ]   =  king    
            self.pieces['Queen'   ]   =  queen   
            self.pieces['Bishop_1']   =  bishop_1
            self.pieces['Bishop_2']   =  bishop_2
            self.pieces['Knight_1']   =  knight_1
            self.pieces['Knight_2']   =  knight_2
            self.pieces['Rook_1'  ]   =  rook_1  
            self.pieces['Rook_2'  ]   =  rook_2  
            self.pieces['Pawn_1'  ]   =  pawn_1  
            self.pieces['Pawn_2'  ]   =  pawn_2  
            self.pieces['Pawn_3'  ]   =  pawn_3  
            self.pieces['Pawn_4'  ]   =  pawn_4  
            self.pieces['Pawn_5'  ]   =  pawn_5  
            self.pieces['Pawn_6'  ]   =  pawn_6  
            self.pieces['Pawn_7'  ]   =  pawn_7  
            self.pieces['Pawn_8'  ]   =  pawn_8  
        else:
            king    = chess.King(_colour,   0, 3,"King")
            queen   = chess.Queen(_colour,  0, 4,"Queen")             
            bishop_1= chess.Bishop(_colour, 0, 2,"Bishop_1")
            bishop_2= chess.Bishop(_colour, 0, 5,"Bishop_2")
            knight_1= chess.Knight(_colour, 0, 1,"Knight_1")
            knight_2= chess.Knight(_colour, 0, 6,"Knight_2")
            rook_1  = chess.Rook(_colour,   0, 0,"Rook_1")
            rook_2  = chess.Rook(_colour,   0, 7,"Rook_2")
            pawn_1  = chess.Pawn_B(_colour, 1, 0,"Pawn_1")
            pawn_2  = chess.Pawn_B(_colour, 1, 1,"Pawn_2")
            pawn_3  = chess.Pawn_B(_colour, 1, 2,"Pawn_3")
            pawn_4  = chess.Pawn_B(_colour, 1, 3,"Pawn_4")
            pawn_5  = chess.Pawn_B(_colour, 1, 4,"Pawn_5")
            pawn_6  = chess.Pawn_B(_colour, 1, 5,"Pawn_6")
            pawn_7  = chess.Pawn_B(_colour, 1, 6,"Pawn_7")
            pawn_8  = chess.Pawn_B(_colour, 1, 7,"Pawn_8")

            
            self.pieces['King'    ]   =  king    
            self.pieces['Queen'   ]   =  queen   
            self.pieces['Bishop_1']   =  bishop_1
            self.pieces['Bishop_2']   =  bishop_2
            self.pieces['Knight_1']   =  knight_1
            self.pieces['Knight_2']   =  knight_2
            self.pieces['Rook_1'  ]   =  rook_1  
            self.pieces['Rook_2'  ]   =  rook_2  
            self.pieces['Pawn_1'  ]   =  pawn_1  
            self.pieces['Pawn_2'  ]   =  pawn_2  
            self.pieces['Pawn_3'  ]   =  pawn_3  
            self.pieces['Pawn_4'  ]   =  pawn_4  
            self.pieces['Pawn_5'  ]   =  pawn_5  
            self.pieces['Pawn_6'  ]   =  pawn_6  
            self.pieces['Pawn_7'  ]   =  pawn_7  
            self.pieces['Pawn_8'  ]   =  pawn_8


    def print_pieces(self):
        for piece in self.pieces.values():
            print(piece.name, str(piece.pos_a), str(piece.pos_b))
    
    def get_colour(self):
        return self.colour

    def kill_piece(self, _piece):
        _piece.kill()
        del self.pieces[_piece.get_name()]

    def take_piece(self, _piece):        
        self.pieces_taken[_piece.get_name()] = _piece

    def get_score(self):
        self.score = len(self.pieces_taken)
        return self.score







