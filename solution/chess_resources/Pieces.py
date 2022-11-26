class Piece(object):
    name = "test"
    is_alive = True

    def __init__(self, _colour, _pos_a, _pos_b):
        self.colour = _colour
        self.pos_a = _pos_a
        self.pos_b = _pos_b

    def print_moves(self):
        for i in range(len(self.possible_moves)):
             print(str(self.possible_moves[i]))

    def get_moves(self):
        return self.possible_moves

    
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

    def change_pos(self, a, b):
        if( a < 0 or a > 7 or b < 0 or b > 7):
            print("Error: Illegal Move.")
            return False
        self.pos_a = a
        self.pos_b = b
        print("Position changed successfully")


#Currently adds illegal positions that are occupied by the same territory. 
    def calculate_moves(self):
        #Make sure we are calculating from the current position.
        for i in range(len(self.possible_moves)):
                self.possible_moves[i][0]   = self.pos_a
                self.possible_moves[i][-1]  = self.pos_b
                pass

        #Iterate through rows
        for i in range(len(self.move_matrix)):
            #Iterate through columns
            for j in range(len(self.move_matrix[0])):

                #Broke these into two if statements for readability, otherwise we would get a super long if statement. 
                #if(The new pos_a is greater than 7 or less than 0) illegal move represented by -1
                if(self.move_matrix[i][j] + self.possible_moves[i][j]) > 7 or (self.move_matrix[i][j] + self.possible_moves[i][j]) < 0:
                    self.possible_moves[i][j] = -1
                    self.possible_moves[i][-1] = -1
                    break
                #if(The new pos_b is greater than 7 or less than 0) illegal move, represented by -1
                elif(self.move_matrix[i][-1] + self.possible_moves[i][-1]) > 7 or (self.move_matrix[i][-1] + self.possible_moves[i][-1]) < 0:
                    self.possible_moves[i][j] = -1
                    self.possible_moves[i][-1] = -1
                    break

                #Legal move, update the moveset. 
                else:
                    self.possible_moves[i][j] = self.move_matrix[i][j] + self.possible_moves[i][j]                

class Pawn_W(Piece):
    name = "White Pawn"
    possible_moves = [[0,0],
                      [0,0],
                      [0,0]]

    move_matrix = [[-1, 0],#March one forward where no enemy blocks path
                   [-1,-1],#Take Top Left where enemy is present
                   [-1, 1]]#Take Top Right where enemy is present

class Pawn_B(Piece):
    name = "Black Pawn"
    possible_moves = [[0,0],
                      [0,0],
                      [0,0]]

    move_matrix = [[1, 0],#March one forward where no enemy blocks path
                   [1, 1],#Take Bottom Right where enemy is present
                   [1,-1]]#Take Bottom Left where enemy is present

class Knight(Piece):
    name = "Knight"
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
    name = "Queen"
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
    name = "Bishop"
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
    name = "Rook"
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
    name = "King"
    #King can move in any direction one space
    #King can't move into a position where he puts himself in danger
    #King can't move into a position that's occupied by friendly piece
    possible_moves = [[0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0],
                      [0,0]]

    move_matrix = [[-1, 1],#Top Right
                   [-1,-1],#Top Left
                   [ 1,-1],#Bottom Left
                   [ 1, 1],#Bottom Right
                   [-1, 0],#Up
                   [ 1, 0],#Down
                   [ 0,-1],#Right 
                   [ 0, 1]]#Left

