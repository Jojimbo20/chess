import chess_resources as chess


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
    def a():
        print("B Well done.")
    
    def get_coords(square):
        pass
    def update():
        #Should get the current positions of the players Pieces and update board[][]
        pass

    def update(self, p1,p2):
        """
            This has become obsolete as p.pieces are now dictionaries
        """

        for piece in p1.pieces.values():
            self.board[piece.get_pos_a()][piece.get_pos_b()] = piece

        for piece in p2.pieces.values():
            self.board[piece.get_pos_a()][piece.get_pos_b()] = piece