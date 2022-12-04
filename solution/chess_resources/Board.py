import chess_resources as chess
print("Board.py accessed")


class Board(object):
    #A matrix of all of the current Pieces.
    """
        The board matrix stores instances of the players pieces

        square = 8 [A,B,C,D,E,F,G,H]   access key example: 
                 7 [A,B,C,D,E,F,G,H]     square[0][4] == E8                    
                 6 [A,B,C,D,E,F,G,H]     square[3][2] == C5
                 5 [A,B,C,D,E,F,G,H]   
                 4 [A,B,C,D,E,F,G,H]   
                 3 [A,B,C,D,E,F,G,H]   
                 2 [A,B,C,D,E,F,G,H]   
                 1 [A,B,C,D,E,F,G,H]   

    """
    board =  [[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]]

    def __init__(self, _p1, _p2):
        self.p1 = _p1
        self.p2 = _p2
        self.update()

    def a():
        print("B Well done.")
    
    def get_coords(square):
        pass
    def update():
        #Should get the current positions of the players Pieces and update board[][]
        pass

    #Update
    def update(self):
        """
            This has become obsolete as p.pieces are now dictionaries
        """
        self.board = [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0]]

        for piece in self.p1.pieces.values():
                self.board[piece.get_pos_a()][piece.get_pos_b()] = piece

        for piece in self.p2.pieces.values():
            self.board[piece.get_pos_a()][piece.get_pos_b()] = piece
    
    def path_is_blocked(self, _piece, _new_a, _new_b):
        """
            Returns True if path is blocked
            Returns False if path is free
        """
        pos_a = _piece.get_pos_a()
        pos_b = _piece.get_pos_b()

        #Moving Down
        if _new_a > pos_a:
            #Moving Right
            if _new_b > pos_b:
                #Moving Down Right
                spaces = abs(_new_a - pos_a)
                for i in range(1,spaces):                        
                    if self.get_space(_piece, pos_a + i, pos_b + i) != "EMPTY":
                        return True 

            elif _new_b < pos_b:
                #Moving Down Left
                spaces = abs(_new_a - pos_a)
                for i in range(1,spaces):                        
                    if self.get_space(_piece, pos_a + i, pos_b - i) != "EMPTY":
                        return True

            elif _new_b == pos_b:
                #Moving Down
                for i in range((pos_a+1), (_new_a - 1),1):
                    if self.get_space(_piece, i, pos_b) != "EMPTY":
                        return True 
        
        #Moving Up
        if _new_a < pos_a:
            if _new_b > pos_b:
                #Diagonal Up Right
                spaces = abs(pos_a - _new_a)
                for i in range(1,spaces):                        
                    if self.get_space(_piece, pos_a - i, pos_b + i) != "EMPTY":
                        return True
            elif _new_b < pos_b:
                #Diagonal Up Left
                spaces = abs(pos_a - _new_a)
                for i in range(1,spaces):                        
                    if self.get_space(_piece, pos_a - i, pos_b - i) != "EMPTY":
                        return True

            elif _new_b == pos_b:
                #Up  
                for i in range((pos_a-1), (_new_a + 1), -1):
                    if self.get_space(_piece, i, pos_b) != "EMPTY":
                        return True
        
        #Moving Left or Right
        if _new_a == pos_a:
            if _new_b > pos_b:
                #Right 
                for i in range((pos_b + 1), (_new_b - 1), 1):
                    if self.get_space(_piece, pos_a, i) != "EMPTY":
                        return True

            elif _new_b < pos_b:
                #Left
                for i in range((pos_b - 1), (_new_b + 1), -1):
                    if self.get_space(_piece, pos_a, i) != "EMPTY":
                        return True

    def get_space(self, _piece, _pos_a, _pos_b):
        """
            Gives you the status of a space relative to a piece            
        """
        space = self.board[_pos_a][_pos_b]

        if space == 0:
            return "EMPTY"
        elif space.get_colour() == _piece.get_colour():
            return "FRIENDLY"
        else:
            return "ENEMY"
        
    def attack_square(self, _pos_a, _pos_b):
        _piece = self.board[_pos_a][_pos_b]
        _piece_colour = _piece.get_colour()
        if _piece == 0:
            print("Attack Error: Square is empty, you messed up the code!")

        elif _piece_colour in self.p1.get_colour():
            self.p2.take_piece(_piece)
            self.p1.kill_piece(_piece)

        elif _piece_colour in self.p2.get_colour():
            self.p1.take_piece(_piece)
            self.p2.kill_piece(_piece)
        
        print("Attack Successful: {piece} has fallen.".format(piece =_piece.get_name()))

    def register_move(self, _piece, _pos_a, _pos_b):
        #Check if move is in bounds
        if _pos_a < 0 or _pos_a > 7:
            print("Illegal move: {piece} to {pos_a},{pos_b} is out of bounds.".format(piece=_piece.get_name(),  pos_a=_pos_a,  pos_b=_pos_b))
        
        #If move is in bounds, check if it's a legal move for the piece. 
        elif self.is_legal_move(_piece, _pos_a, _pos_b):
            _piece.change_pos(_pos_a,_pos_b)
            print("Move successful! {piece} now has position: {pos_a},{pos_b}".format(piece=_piece.get_name(),  pos_a=_piece.get_pos_a(),  pos_b=_piece.get_pos_b()))
            self.update()

    def is_legal_move(self, _piece, _new_a, _new_b):
        """
            The legal move checker only needs to have specific rules for a few of the pieces:
            Pawn: 
                Can't march if the space infront is occupied DONE
                Can only move diagonally if the space is occupied by enemy. DONE

            Queen, Rook and Bishop: 
                Can't move through a piece 
            King:
                Can't put himself into danger. 
        """
        #Retrieve the thing that is in the desired space
        space = self.get_space(_piece, _new_a, _new_b)
        piece_name = _piece.get_name()

        #Check to see if the piece is dead.
        if _piece.is_alive() != True:
            print("Illegal Move: {piece} has been felled".format(piece=piece_name))
            return False

        #Calulate possible moves based on position and move matrix
        self.calculate_moves(_piece)     

        #Checks if it's in the pieces moveset
        if _piece.is_in_moveset(_new_a, _new_b):            

            #Check the desired space is empty:
            if space == "EMPTY":                
                #Pawn attempts to attack empty square: Dissallowed
                if "Pawn" in piece_name and (_new_b != _piece.get_pos_b()):
                    print("Illegal Move: Pawn cannot attack empty square")
                    return False
                if "Bishop" in piece_name and self.path_is_blocked(_piece,_new_a,_new_b):
                    print("Illegal Move: Bishop's Path is blocked")
                    return False
                if "Queen" in piece_name and self.path_is_blocked(_piece,_new_a,_new_b):
                    print("Illegal Move: Queens's Path is blocked")
                    return False
                if "Rook" in piece_name and self.path_is_blocked(_piece,_new_a,_new_b):
                    print("Illegal Move: Rooks's Path is blocked")
                    return False

                return True

            #Space is occupied by enemy, Take piece add it to players taken pieces, take it away from players pieces
            elif space == "ENEMY":
                if "Pawn" in piece_name and (_new_b == _piece.get_pos_b()):
                    print("Illegal Move: Pawn cannot attack Forward")
                    return False

                self.attack_square(_new_a, _new_b)
                return True

            #Space is occupied by friendly: Illegal move
            elif space == "FRIENDLY":
                print("Illegal Move: Space occupied by friendly.")
                return False
            
        print("Illegal Move: {piece} has no possible move ".format(piece=piece_name))
        return False        

    #Currently adds illegal positions that are occupied by the same territory. 
    def calculate_moves(self, _piece):
        #Make sure we are calculating from the current position.
        for row_index in range(len(_piece.possible_moves)):
                _piece.possible_moves[row_index][0]   = _piece.pos_a
                _piece.possible_moves[row_index][-1]  = _piece.pos_b


        #Iterate through rows
        for row_index in range(len(_piece.move_matrix)):
            #Iterate through columns
            for column_index in range(len(_piece.move_matrix[0])):

                ####THESE HANDLE OUT OF BOUNDS CASES
                #Broke these into two if statements for readability, otherwise we would get a super long if statement. 
                #if(The new pos_a is greater than 7 or less than 0) illegal move represented by -1
                if(_piece.move_matrix[row_index][column_index] + _piece.possible_moves[row_index][column_index]) > 7 or (_piece.move_matrix[row_index][column_index] + _piece.possible_moves[row_index][column_index]) < 0:
                    _piece.possible_moves[row_index][column_index] = -1
                    _piece.possible_moves[row_index][-1] = -1
                    break
                #if(The new pos_b is greater than 7 or less than 0) illegal move, represented by -1
                elif(_piece.move_matrix[row_index][-1] + _piece.possible_moves[row_index][-1]) > 7 or (_piece.move_matrix[row_index][-1] + _piece.possible_moves[row_index][-1]) < 0:
                    _piece.possible_moves[row_index][column_index] = -1
                    _piece.possible_moves[row_index][-1] = -1
                    break

                #Legal move, update the moveset. 
                else:
                    _piece.possible_moves[row_index][column_index] = _piece.move_matrix[row_index][column_index] + _piece.possible_moves[row_index][column_index]        

