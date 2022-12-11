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

    valid_names = ("King","Queen",
                   "Bishop_1","Bishop_2",
                   "Knight_1","Knight_2",
                   "Rook_1","Rook_2",
                   "Pawn_1","Pawn_2",
                   "Pawn_3","Pawn_4",
                   "Pawn_5","Pawn_6",
                   "Pawn_7","Pawn_8")

    move_counter = {"Total_Moves":0}

    def __init__(self):
        self.p1 = chess.Player("White")
        self.p2 = chess.Player("Black")
        self.update()




        
    def update(self):
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
        return False






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
        
        print("Attack Successful: {player} {piece} has fallen.".format(player=_piece.get_colour(), piece =_piece.get_name()))



    def is_valid_name(self, _piece):    
        for name in self.valid_names:
            if _piece in name:
                return True        
        return False
                            


    def king_check_printer(self):
        if self.p1.pieces["King"].check == True:
            print("White's King is in Check.")
        
        elif self.p2.pieces["King"].check == True:            
            print("Black's King is in Check.")

    def register_move(self, _player, _piece, _pos_a, _pos_b):
        if "White" in _player:
            player = self.p1
        elif "Black" in _player:
            player = self.p2
        else:
            print("{entry} is an invalid player. Please enter 'White' or 'Black'.".format(entry=_player))
            return
            
        if self.is_valid_name(_piece) != True:
            print("Name invalid, please enter a valid name from the list: {names}".format(names=self.valid_names))
            return

        piece = player.pieces[_piece]


        print("\nAttempting {player} {piece} to {pos_a} {pos_b}".format(player=_player, piece=_piece, pos_a =_pos_a, pos_b=_pos_b))
        #Check if move is in bounds
        if _pos_a < 0 or _pos_a > 7:
            print("Illegal move: {piece} to {pos_a},{pos_b} is out of bounds.".format(piece=piece.get_name(),  pos_a=_pos_a,  pos_b=_pos_b))
            return
        
        elif player.pieces["King"].check == True:
            if self.puts_king_in_check(piece, _pos_a, _pos_b) == True:
                print("Illegal move: King is currently in check.\n")
            elif self.is_legal_move(piece, _pos_a, _pos_b):
                print("Move successful! {player} {piece} now has position: {pos_a},{pos_b}".format(player=_player, piece=_piece, pos_a =_pos_a, pos_b=_pos_b))
                self.uncheck_self(piece)
                self.update()
                return
        
        #If move is in bounds, check if it's a legal move for the piece. 
        elif self.is_legal_move(piece, _pos_a, _pos_b):
            piece.change_pos(_pos_a,_pos_b)
            print("Move successful! {player} {piece} now has position: {pos_a},{pos_b}".format(player=_player, piece=_piece, pos_a =_pos_a, pos_b=_pos_b))
            self.king_check_printer()
            self.update()
            return


    def puts_king_in_check(self, _piece, _new_a, _new_b):
            #Save the piece that's on the board so that we can reset it later 
            save_piece = self.board[_new_a][_new_b]

            #Finalize the move on the board
            self.board[_piece.get_pos_a()][_piece.get_pos_b()] = 0            
            self.board[_new_a][_new_b] = _piece

            if "White" in _piece.get_colour():
                enemy_pieces = self.p2.pieces
                king_pos = [0,0]

                #If the King is moving, then we need the kings new coordinates
                if "King" in _piece.get_name():
                    king_pos[0] = _new_a
                    king_pos[1] = _new_b
                    
                #Otherwise we need the Kings current coordinates
                else:
                    king = self.p1.pieces["King"]
                    king_pos[0] = king.get_pos_a()
                    king_pos[1] = king.get_pos_b()

                for piece in enemy_pieces.values():
                    self.calculate_moves(piece)

                    #Pawns can't attack diagonally so no poin't calculting their moves if king is infront of them
                    if "Pawn" in piece.get_name() and possible_move[1] == king_pos[1]:
                        continue

                    #For each enemy piece, check the possible moves to see if any of them match with the Kings postion 
                    for possible_move in piece.possible_moves:
                        if possible_move == king_pos and self.path_is_blocked(piece, possible_move[0],possible_move[1]) == False:

                            #Reset the board to it's original state
                            self.board[_new_a][_new_b] = save_piece
                            self.board[_piece.get_pos_a()][_piece.get_pos_b()] = _piece
                            return True

            elif "Black" in _piece.get_colour():                
                enemy_pieces = self.p1.pieces                
                king_pos = [0,0]

                #If the King is moving, then we need the kings new coordinates
                if "King" in _piece.get_name():
                    king_pos[0] = _new_a
                    king_pos[1] = _new_b

                #Otherwise we need the Kings current coordinates
                else:
                    king = self.p2.pieces["King"]
                    king_pos[0] = king.get_pos_a()
                    king_pos[1] = king.get_pos_b()

                for piece in enemy_pieces.values():
                    self.calculate_moves(piece)

                    #Pawns can't attack diagonally so no poin't calculting their moves if king is infront of them
                    if "Pawn" in piece.get_name() and piece.get_pos_b() == king_pos[1]:
                        continue

                    #For each enemy piece, check the possible moves to see if any of them match with the Kings postion
                    for possible_move in piece.possible_moves:
                        if possible_move == king_pos and self.path_is_blocked(piece, possible_move[0],possible_move[1]) == False:
                            #Reset the board to it's original state
                            self.board[_new_a][_new_b] = save_piece
                            self.board[_piece.get_pos_a()][_piece.get_pos_b()] = _piece
                            return True

            #Reset the board to it's original state
            self.board[_new_a][_new_b] = save_piece
            self.board[_piece.get_pos_a()][_piece.get_pos_b()] = _piece           
            return False


    def puts_enemy_king_in_check(self, _piece, _new_a, _new_b):
            #Make a copy of the board with the new move finalised
            old_pos_a = _piece.get_pos_a()
            old_pos_b = _piece.get_pos_b()
            self.board[old_pos_a][old_pos_b] = 0
            _piece.change_pos(_new_a, _new_b)            
            self.board[_new_a][_new_b] = _piece

            if "White" in _piece.get_colour():
                pieces = self.p1.pieces
                enemy_king = self.p2.pieces["King"]
                enemy_king_pos = [0,0]
                enemy_king_pos[0] = enemy_king.get_pos_a()
                enemy_king_pos[1] = enemy_king.get_pos_b()

                for piece in pieces.values():
                    self.calculate_moves(piece)

                    #Pawns can't attack diagonally so no poin't calculting their moves if king is infront of them
                    if "Pawn" in piece.get_name() and piece.get_pos_b() == enemy_king_pos[1]:
                        continue

                    for possible_move in piece.possible_moves:
                        if possible_move == enemy_king_pos and self.path_is_blocked(piece, possible_move[0],possible_move[1]) == False:
                            self.board[_new_a][_new_b] = 0
                            _piece.change_pos(old_pos_a,old_pos_b)
                            self.board[old_pos_a][old_pos_b] = _piece
                            return True

            elif "Black" in _piece.get_colour():                
                pieces = self.p2.pieces
                enemy_king = self.p1.pieces["King"]
                enemy_king_pos = [0,0]
                enemy_king_pos[0] = enemy_king.get_pos_a()
                enemy_king_pos[1] = enemy_king.get_pos_b()

                for piece in pieces.values():
                    self.calculate_moves(piece)

                    #Pawns can't attack diagonally so no poin't calculting their moves if king is infront of them
                    if "Pawn" in piece.get_name() and piece.get_pos_b() == enemy_king_pos[1]:
                        continue

                    for possible_move in piece.possible_moves:
                        if possible_move == enemy_king_pos and self.path_is_blocked(piece, possible_move[0],possible_move[1]) == False:

                            #Reset the board to it's original state
                            self.board[_new_a][_new_b] = 0
                            _piece.change_pos(old_pos_a,old_pos_b)
                            self.board[old_pos_a][old_pos_b] = _piece
                            return True

            #Reset the board to it's original state
            self.board[_new_a][_new_b] = 0
            _piece.change_pos(old_pos_a,old_pos_b)
            self.board[old_pos_a][old_pos_b] = _piece
            return False

    def check_enemy(self, _piece):
        if "White" in _piece.get_colour():
            self.p2.pieces["King"].check = True

        elif "Black" in _piece.get_colour():             
            self.p1.pieces["King"].check = True

    def uncheck_self(self, _piece):
        if "White" in _piece.get_colour():
            self.p1.pieces["King"].check = False

        elif "Black" in _piece.get_colour():             
            self.p2.pieces["King"].check = False

    def is_legal_move(self, _piece, _new_a, _new_b):
        ##############
        # EXIT CASES #
        ############## 

        #Get the piece name for easier referencing 
        piece_name = _piece.get_name()
             
        #1) Piece is dead
        if _piece.is_alive() != True:            
            print("Illegal Move: {piece} has been felled".format(piece=piece_name))
            return False

        #2) Illegal move pattern
        #Calulate possible moves based on position and move matrix then check if the move is in the moveset
        self.calculate_moves(_piece)   
        if _piece.is_in_moveset(_new_a, _new_b) != True:            
            print("Illegal Move: {piece} has no possible move ".format(piece=piece_name))
            return False
        
        ##################
        # RULE CHECKING: #
        ##################

        #Get status of the desired space: "EMPTY" "FRIENDLY "ENEMY"
        space = self.get_space(_piece, _new_a, _new_b)

        #Space is occupied by friendly: Illegal move
        if space == "FRIENDLY":
            print("Illegal Move: Space occupied by friendly.")
            return False

        ############################
        # MOVING INTO EMPTY SPACE: #
        ############################
        elif space == "EMPTY":
        
            #Rule: Move can't put your king in check
            if self.puts_king_in_check(_piece, _new_a, _new_b) == True:
                print("Illegal Move: Move puts King in check")
                return False
        
            #Rule: Pieces can't move through other pieces with the exeption of Knights
            elif "Knight" not in piece_name and self.path_is_blocked(_piece,_new_a,_new_b):
                print("Illegal Move: {piece}'s Path is blocked".format(piece=piece_name))
                return False
        
            #Pawns have two rules
            elif "Pawn" in piece_name:        
                
                #Rule 1: Pawns can only move diagonally when attacking
                if _new_b != _piece.get_pos_b():
                    print("Illegal Move: Pawn cannot attack empty square")
                    return False
        
                #Rule 2: Pawn can move two spaces on the first turn only
                elif _piece.first_turn == True:
                    
                    #Removes the ability to move two forward after 1st move
                    _piece.first_turn_complete()

            #Check if move puts enemy king in check
            if self.puts_enemy_king_in_check(_piece, _new_a, _new_b) == True:                
                self.check_enemy(_piece)
        
            #Checks passed, move is legal. 
            return True
        
        ######################
        # ATTACKING A SPACE: #
        ######################
        elif space == "ENEMY":

            #Rule: Pawns can't attack forward. 
            if "Pawn" in piece_name and (_new_b == _piece.get_pos_b()):
                print("Illegal Move: Pawn cannot attack Forward")
                return False
            #Check if move puts enemy king in check
            if self.puts_enemy_king_in_check(_piece, _new_a, _new_b) == True:
                self.check_enemy(_piece)
            
            #Legal attack
            self.attack_square(_new_a, _new_b)
            return True
        

            
                







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

