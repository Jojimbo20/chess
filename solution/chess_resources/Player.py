import chess_resources as chess
class Player(object):
    #The number of Pieces 
    def __init__(self, _colour):  
        self.colour = _colour
        self.pieces = []

        if _colour != "White" and _colour != "Black":
            print("ERROR: Colour must be 'White' or 'Black'")
        elif _colour == "White":
            colour = _colour
            king    = chess.King(_colour,   7, 3)
            queen   = chess.Queen(_colour,  7, 4)             
            bishop_1= chess.Bishop(_colour, 7, 2)
            bishop_2= chess.Bishop(_colour, 7, 5)
            knight_1= chess.Knight(_colour, 7, 1)
            knight_2= chess.Knight(_colour, 7, 6)
            rook_1  = chess.Rook(_colour,   7, 0)
            rook_2  = chess.Rook(_colour,   7, 7)
            pawn_1  = chess.Pawn_W(_colour, 6, 0)
            pawn_2  = chess.Pawn_W(_colour, 6, 1)
            pawn_3  = chess.Pawn_W(_colour, 6, 2)
            pawn_4  = chess.Pawn_W(_colour, 6, 3)
            pawn_5  = chess.Pawn_W(_colour, 6, 4)
            pawn_6  = chess.Pawn_W(_colour, 6, 5)
            pawn_7  = chess.Pawn_W(_colour, 6, 6)
            pawn_8  = chess.Pawn_W(_colour, 6, 7)

            
            self.pieces.append(king    )
            self.pieces.append(queen   )
            self.pieces.append(bishop_1)
            self.pieces.append(bishop_2)
            self.pieces.append(knight_1)
            self.pieces.append(knight_2)
            self.pieces.append(rook_1  )
            self.pieces.append(rook_2  )
            self.pieces.append(pawn_1  )
            self.pieces.append(pawn_2  )
            self.pieces.append(pawn_3  )
            self.pieces.append(pawn_4  )
            self.pieces.append(pawn_5  )
            self.pieces.append(pawn_6  )
            self.pieces.append(pawn_7  )
            self.pieces.append(pawn_8  )
        else:
            king    = chess.King(_colour,   0, 3)
            queen   = chess.Queen(_colour,  0, 4)             
            bishop_1= chess.Bishop(_colour, 0, 2)
            bishop_2= chess.Bishop(_colour, 0, 5)
            knight_1= chess.Knight(_colour, 0, 1)
            knight_2= chess.Knight(_colour, 0, 6)
            rook_1  = chess.Rook(_colour,   0, 0)
            rook_2  = chess.Rook(_colour,   0, 7)
            pawn_1  = chess.Pawn_B(_colour, 1, 0)
            pawn_2  = chess.Pawn_B(_colour, 1, 1)
            pawn_3  = chess.Pawn_B(_colour, 1, 2)
            pawn_4  = chess.Pawn_B(_colour, 1, 3)
            pawn_5  = chess.Pawn_B(_colour, 1, 4)
            pawn_6  = chess.Pawn_B(_colour, 1, 5)
            pawn_7  = chess.Pawn_B(_colour, 1, 6)
            pawn_8  = chess.Pawn_B(_colour, 1, 7)

            
            self.pieces.append(king    )
            self.pieces.append(queen   )
            self.pieces.append(bishop_1)
            self.pieces.append(bishop_2)
            self.pieces.append(knight_1)
            self.pieces.append(knight_2)
            self.pieces.append(rook_1  )
            self.pieces.append(rook_2  )
            self.pieces.append(pawn_1  )
            self.pieces.append(pawn_2  )
            self.pieces.append(pawn_3  )
            self.pieces.append(pawn_4  )
            self.pieces.append(pawn_5  )
            self.pieces.append(pawn_6  )
            self.pieces.append(pawn_7  )
            self.pieces.append(pawn_8  )


    def print_pieces(self):
        for piece in self.pieces:
            print(piece.name, str(piece.pos_a), str(piece.pos_b))
    pass




