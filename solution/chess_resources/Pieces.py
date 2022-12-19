print("Pieces.py accessed")
class Piece(object):
    name = ""
    is_alive = True
    possible_moves = []
    first_turn = True

    def __init__(self, _colour, _pos_a, _pos_b, _name):
        self.colour = _colour
        self.name = _name
        self.pos_a = _pos_a
        self.pos_b = _pos_b
        

    def print_moves(self):
        for i in range(len(self.possible_moves)):
             print(str(self.possible_moves[i]))

    def get_moves(self):
        return self.possible_moves

    def get_name(self):
        """
            return self.name 
        """
        return self.name

    def get_pos_a(self):
        """
            return self.pos_a
        """
        return int(self.pos_a)
        
    def get_pos_b(self):
        """
            return self.pos_b
        """
        return int(self.pos_b)

    def get_colour(self):
        """
            return self.colour
        """
        return str(self.colour)

    def change_pos(self, a, b):
        if( a < 0 or a > 7 or b < 0 or b > 7):
            print("Error: Illegal Move.")
            return False
        self.pos_a = a
        self.pos_b = b
        #print("Position changed successfully")

    def is_in_moveset(self, _pos_a, _pos_b):
        for pos in self.possible_moves:
                if pos[0] == _pos_a and pos[1] == _pos_b:
                    return True
        return False
    
    def first_turn_complete(self):
        self.first_turn = False

    def kill(self):
        self.is_alive = False

    def is_alive(self):
        if self.is_alive:
            return True
        return False



class Pawn_W(Piece):
    def __init__(self, _colour, _pos_a, _pos_b, _name):        
        self.colour = _colour
        self.name = _name
        self.pos_a = _pos_a
        self.pos_b = _pos_b
        self.passant = False
        self.passant_victim_pos_a = -1
        self.passant_victim_pos_b = -1

        self.possible_moves = [[0,0],
                               [0,0],
                               [0,0],
                               [0,0]]

        self.move_matrix = [[-2, 0],#March two forward where no enemy blocks path and first_turn = True
                            [-1, 0],#March one forward where no enemy blocks path
                            [-1,-1],#Take Top Left where enemy is present
                            [-1, 1]]#Take Top Right where enemy is present    

    def first_turn_complete(self):
        del self.possible_moves[0]
        del self.move_matrix[0]        
        self.first_turn = False
        
    def can_passant(self, _new_a, _new_b):
        self.passant = True
        self.passant_victim_pos_a = _new_a
        self.passant_victim_pos_b = _new_b


    def can_not_passant(self):
        self.passant = False
        self.passant_victim_pos_a = -1
        self.passant_victim_pos_b = -1



class Pawn_B(Piece):
    def __init__(self, _colour, _pos_a, _pos_b, _name):        
        self.colour = _colour
        self.name = _name
        self.pos_a = _pos_a
        self.pos_b = _pos_b
        self.passant = False
        self.passant_victim_pos_a = -1
        self.passant_victim_pos_b = -1

        self.possible_moves = [[0,0],
                               [0,0],
                               [0,0],
                               [0,0]]

        self.move_matrix = [[2, 0],#March two forward where no enemy blocks path and first_turn = True
                            [1, 0],#March one forward where no enemy blocks path
                            [1, 1],#Take Bottom Right where enemy is present
                            [1,-1]]#Take Bottom Left where enemy is present

    def first_turn_complete(self):
        del self.possible_moves[0]
        del self.move_matrix[0]        
        self.first_turn = False

    def can_passant(self, _new_a, _new_b):
        self.passant = True
        self.passant_victim_pos_a = _new_a
        self.passant_victim_pos_b = _new_b


    def can_not_passant(self):
        self.passant = False
        self.passant_victim_pos_a = -1
        self.passant_victim_pos_b = -1


class Knight(Piece):
    possible_moves = [[0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0]]

    #Must be on the board
    #New position must not be occupied by friendly
    move_matrix = [[-2,-1],
                   [-2, 1],
                   [-1,-2],
                   [-1, 2],
                   [ 1,-2],
                   [ 1, 2],
                   [ 2,-1],
                   [ 2, 1]]

class Queen(Piece):
    possible_moves = [[0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0]]

    #Queen can move in any direction as long as path is not blocked
    move_matrix = [[-1, 0],#Up
                   [-2, 0],
                   [-3, 0],
                   [-4, 0],
                   [-5, 0],
                   [-6, 0],
                   [-7, 0],
                   [ 1, 0],#Down
                   [ 2, 0],
                   [ 3, 0],
                   [ 4, 0],
                   [ 5, 0],
                   [ 6, 0],
                   [ 7, 0],
                   [ 0,-1],#Left
                   [ 0,-2],
                   [ 0,-3],
                   [ 0,-4],
                   [ 0,-5],
                   [ 0,-6],
                   [ 0,-7],
                   [ 0, 1],#Right
                   [ 0, 2],
                   [ 0, 3],
                   [ 0, 4],
                   [ 0, 5],
                   [ 0, 6],
                   [ 0, 7],
                   [-1,-1],#Top Left
                   [-2,-2],
                   [-3,-3],
                   [-4,-4],
                   [-5,-5],
                   [-6,-6],
                   [-7,-7],
                   [ 1, 1],#Bottom Right
                   [ 2, 2],
                   [ 3, 3],
                   [ 4, 4],
                   [ 5, 5],
                   [ 6, 6],
                   [ 7, 7],
                   [-1, 1],#Top Right
                   [-2, 2],
                   [-3, 3],
                   [-4, 4],
                   [-5, 5],
                   [-6, 6],
                   [-7, 7],
                   [ 1,-1],#Bottom Left
                   [ 2,-2],
                   [ 3,-3],
                   [ 4,-4],
                   [ 5,-5],
                   [ 6,-6],
                   [ 7,-7]]

class Bishop(Piece):
    #Bishop can move diagonally as long as path is not blocked 
    possible_moves = [[0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0]]

    move_matrix = [[-1,-1],#Top Left
                   [-2,-2],
                   [-3,-3],
                   [-4,-4],
                   [-5,-5],
                   [-6,-6],
                   [-7,-7],
                   [ 1, 1],#Bottom Right
                   [ 2, 2],
                   [ 3, 3],
                   [ 4, 4],
                   [ 5, 5],
                   [ 6, 6],
                   [ 7, 7],
                   [-1, 1],#Top Right
                   [-2, 2],
                   [-3, 3],
                   [-4, 4],
                   [-5, 5],
                   [-6, 6],
                   [-7, 7],
                   [ 1,-1],#Bottom Left
                   [ 2,-2],
                   [ 3,-3],
                   [ 4,-4],
                   [ 5,-5],
                   [ 6,-6],
                   [ 7,-7]]


class Rook(Piece):
    #Rook can move up down left right as long as path is not blocked 
    possible_moves = [[0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0]]

    move_matrix = [[-1, 0],#Up
                   [-2, 0],
                   [-3, 0],
                   [-4, 0],
                   [-5, 0],
                   [-6, 0],
                   [-7, 0],
                   [ 1, 0],#Down
                   [ 2, 0],
                   [ 3, 0],
                   [ 4, 0],
                   [ 5, 0],
                   [ 6, 0],
                   [ 7, 0],
                   [ 0,-1],#Left
                   [ 0,-2],
                   [ 0,-3],
                   [ 0,-4],
                   [ 0,-5],
                   [ 0,-6],
                   [ 0,-7],
                   [ 0, 1],#Right
                   [ 0, 2],
                   [ 0, 3],
                   [ 0, 4],
                   [ 0, 5],
                   [ 0, 6],
                   [ 0, 7]]

class King(Piece):
    """
       King can move in any direction one space
       King can't move into a position where he puts himself in danger
       King can't move into a position that's occupied by friendly piece
       King has a special move: Castling
    """

    def __init__(self, _colour, _pos_a, _pos_b, _name):
        self.colour = _colour
        self.name = _name
        self.pos_a = _pos_a
        self.pos_b = _pos_b
        self.check = False
        self.possible_moves = [[0,0],
                               [0,0],
                               [0,0],
                               [0,0],
                               [0,0],
                               [0,0],
                               [0,0],
                               [0,0],
                               [0,0],
                               [0,0]]
    
        self.move_matrix = [[ 0,-2],#Left Two (CASTLE ONLY)
                            [ 0, 2],#Right Two (CASTLE ONLY)
                            [-1, 1],#Top Right
                            [-1,-1],#Top Left
                            [ 1,-1],#Bottom Left
                            [ 1, 1],#Bottom Right
                            [-1, 0],#Up
                            [ 1, 0],#Down
                            [ 0,-1],#Left
                            [ 0, 1]]#Right


    def first_turn_complete(self):
        del self.possible_moves[0]
        del self.possible_moves[0]
        del self.move_matrix[0]
        del self.move_matrix[0]
        self.first_turn = False

    

