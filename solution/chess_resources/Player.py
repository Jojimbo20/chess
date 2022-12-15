import chess_resources as chess
print("Player.py accessed")

class Player(object):
    #The number of Pieces 
    score = 0
    valid_names = ("King","Queen","Bishop_1","Bishop_2","Knight_1","Knight_2","Rook_1","Rook_2","Pawn_1","Pawn_2","Pawn_3","Pawn_4","Pawn_5","Pawn_6","Pawn_7","Pawn_8")

    def __init__(self, _colour):  
        self.colour = _colour
        self.pieces = {}
        self.pieces_taken = {}
        self.pieces_promoted = {}

        if _colour != "White" and _colour != "Black":
            print("ERROR: Colour must be 'White' or 'Black'")
        elif _colour == "White":
            king    = chess.King(_colour,   7, 4,"King")
            queen   = chess.Queen(_colour,  7, 3,"Queen")             
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
            king    = chess.King(_colour,   0, 4,"King")
            queen   = chess.Queen(_colour,  0, 3,"Queen")             
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
            print(piece.colour, piece.name,"\t", str(piece.pos_a), str(piece.pos_b))
        print("Total pieces alive: {num_of_pieces}".format(num_of_pieces=len(self.pieces)))
    
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

    def add_piece(self, _piece, _pos_a, _pos_b):
        if self.is_legal_pos(_pos_a,_pos_b) == False:
            print("Illegal piece position: Are pos_a and pos_b within 0 and 7?")
            return

        instances = self.get_instances(_piece)
        new_name = _piece + "_" + str(instances+1)

        if "Queen" in new_name:
            self.pieces[new_name] = chess.Queen(self.get_colour(),_pos_a, _pos_b, new_name)
        elif "Bishop" in new_name:
            self.pieces[new_name] = chess.Bishop(self.get_colour(),_pos_a, _pos_b, new_name)
        elif "Knight" in new_name:
            self.pieces[new_name] = chess.Knight(self.get_colour(),_pos_a, _pos_b, new_name)
        elif "Rook" in new_name:
            self.pieces[new_name] = chess.Rook(self.get_colour(),_pos_a, _pos_b, new_name)

    def promote_pawn(self, pawn, new_piece):
        if "Pawn" not in pawn.get_name():
            print("{name} cannot be promoted. Only Pawns can be promoted.".format(name=pawn.get_name()))
            return
        
        self.add_piece(new_piece, pawn.get_pos_a(), pawn.get_pos_b())
        self.pieces_promoted[pawn.get_name()] = pawn
        self.kill_piece(pawn)
    
    def get_piece_names(self):
        names = []
        for piece_name in self.pieces:
            names.append(piece_name)

        return names


    def is_legal_pos(self, _pos_a, _pos_b):
        if _pos_a < 0 or _pos_b < 0 or _pos_a > 7 or _pos_b > 7:
            return False
        return True

    def is_legal_name(self, _name):
        for piece_name in self.valid_names:
            if _name == piece_name:
                return True
        return False

    def get_instances(self, _piece):
        if self.is_legal_name(_piece) != True:
            print("{name} is not a valid piece name. Please enter a valid piece name: \n{valid_names}".format(name=_piece,valid_names=self.valid_names))
            return 

        instance_counter = 0
        for piece in self.pieces.values():
            if _piece in piece.get_name():
                instance_counter += 1

        return instance_counter

    def get_live_names(self):
        names_string = ""
        for name in self.pieces:
            names_string += name + ", "

        names_string.rstrip()
        return names_string






