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

    def register_move(self, _piece, _pos_a, _pos_b):
        if _pos_a < 0 or _pos_a > 7:
            print("Illegal move: {piece} to {pos_a},{pos_b} is out of bounds.".format(piece=_piece.get_name(),pos_a=_pos_a,pos_b=_pos_b))
        if self.is_legal_move(_piece, _pos_a, _pos_b):
            piece = self.pieces[_piece]
            piece.change_pos(_pos_a,_pos_b)
            print("Move successful! {piece} now has position: {pos_a},{pos_b}".format(piece=_piece.get_name(),pos_a=_piece.get_pos_a(),pos_b=_piece.get_pos_b()))

    def is_legal_move(self, _piece, _pos_a, _pos_b):
        #Calulate possible moves based on position and move matrix
        self.update()
        self.calculate_moves(_piece)
        
        #Retrieve the thing that is in the desired square
        square = self.board[_pos_a][_pos_b]

        #If the square is empty, or the square is ocupied by enemy,
        #Check that it's within the bounds of movement 
        if square == 0 or square.get_colour() != _piece.get_colour(): 
            for pos in _piece.possible_moves:
                if pos[0] == _pos_a and pos[1] == _pos_b:
                    return True
            print("Illegal Move: {piece} has no possible move ".format(piece=_piece.get_name()))

        elif square.get_colour() == _piece.get_colour():
            print("Illegal Move: Space occupied by friendly.")
            return False

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

