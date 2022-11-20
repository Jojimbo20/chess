from turtle import position


class Piece(object):
    is_alive = True
    pos_a = 0
    pos_b = 0

    def __init__(self, _name, _colour, _pos_a, _pos_b):
        self.name = _name
        self.colour = _colour
        self.pos_a = _pos_a
        self.pos_b = _pos_b

class Pawn(Piece):
    name = "Pawn"
    possible_moves = [0][0]
    move_matrix = [0][0]

    def calculate_moves():
        print("Calculating moves...")
        pass

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

    move_matrix = [[-2,-1],
                   [-2, 1],
                   [-1,-2],
                   [-1, 2],
                   [ 1,-2],
                   [ 1, 2],
                   [ 2,-1],
                   [ 2, 1]]

    def calculate_moves(self):
        #self.position[][]

        for i in range(len(self.move_matrix)):
            #iterate through columns
            for j in range(len(self.move_matrix[0])):
                self.possible_moves[i][j] = self.move_matrix[i][j] + self.possible_moves[i][j]

    def print_moves(self):
        for i in range(len(self.move_matrix)):
            #iterate through columns
            for j in range(len(self.move_matrix[0])):
                print(str(self.possible_moves[i][j]))

    def change_pos(self, a, b):
        self.pos_a = a
        self.pos_b = b



