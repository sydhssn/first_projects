import os
os.system("clear")

class Board:
    def __init__(self):
        self.state = [['?', '?', '?'],
        ['?', '?', '?'],
        ['?', '?', '?']]
    
    def display(self):
        print(" %s | %s | %s" %(self.state[0][0], self.state[0][1], self.state[0][2]))
        print("-----------") 
        print(" %s | %s | %s" %(self.state[1][0], self.state[1][1], self.state[1][2]))
        print("-----------") 
        print(" %s | %s | %s" %(self.state[2][0], self.state[2][1], self.state[2][2]))

    def update_state(self, row, column, player):
        if self.state[row][column] == '?':
            self.state[row][column] = player 
    
    def is_winner(self, player):
        # horizontal
        if self.state[0][0] == self.state[0][1] == self.state[0][2] != '?':
            return True
        elif self.state[1][0] == self.state[1][1] == self.state[1][2] != '?':
            return True    
        elif self.state[2][0] == self.state[2][1] == self.state[2][2] != '?':
            return True
        # vertical
        elif self.state[0][0] == self.state[1][0] == self.state[2][0] != '?':
            return True
        elif self.state[0][1] == self.state[1][1] == self.state[2][1] != '?':
            return True
        elif self.state[0][2] == self.state[1][2] == self.state[2][2] != '?':
            return True
        # diagonal
        elif self.state[0][0] == self.state[1][1] == self.state[2][2] != '?':
            return True
        elif self.state[0][2] == self.state[1][1] == self.state[2][0] != '?':
            return True
        else:
            return False

    # no winner yet
    def no_winner_yet(self, player):
        if self.state[0][0] == '?' or self.state[0][1] == '?' or self.state[0][2] == '?' or self.state[1][0] == '?' or self.state[1][1] == '?' or self.state[1][2] == '?' or self.state[2][0] == '?' or self.state[2][1] == '?' or self.state[2][2] == '?':
            return True
        else:
            return False

    #def is_tie(self): # this will keep count of the number of spaces used in the game allowing you to know if a tie condition has been filled.  
        #used_cells = 0
        #for cell in self.state:
            #if cell != '?':
                #used_cells += 1
        #if used_cells == 9:
            #return True
        #else:
            #return False
    
     # the Tie instance: this will keep count of the number of spaces used in the game allowing you to know if a tie condition has been filled.  
    def is_tie(self):
        length_of_state = self.new_method()
        
        #if length_of_state(self) == 9:
        if length_of_state == 9:
            return True
        else:
            return False

    def new_method(self):
        #new_board_count = self.state
        def length_of_state(new_board_count = self.state):
            used_cells = 0
            for row in new_board_count:
                if type(row) == list:
                    for innard in row:
                        if innard != '?':
                            used_cells += length_of_state(innard)
                    #'?'
                else:
                    used_cells += 1
        return length_of_state



    # no winner yet
    def no_winner_yet(self, player):
        if self.state[0][0] == '?' or self.state[0][1] == '?' or self.state[0][2] == '?' or self.state[1][0] == '?' or self.state[1][1] == '?' or self.state[1][2] == '?' or self.state[2][0] == '?' or self.state[2][1] == '?' or self.state[2][2] == '?':
            return True
        else:
            return False
    
    def reset(self):
        self.state = [['?', '?', '?'],
        ['?', '?', '?'],
        ['?', '?', '?']]

board = Board()

def print_header():
    print("Tic-Tac-Toe")

def refresh_screen():
    #clears the screen
    os.system("clear")

    print_header()
    board.display()

while True:
    refresh_screen()
    
    if board.no_winner_yet('O'):
        print('No winner yet')

    # X goes
    x_column_choice = int(input("\n X - please choose column 1-3. > "))-1
    x_row_choice = int(input("\n X - please choose row 1-3. > "))-1
    # update board with X
    board.update_state(x_row_choice, x_column_choice, 'X')

    # refresh screen
    refresh_screen()

    # X winner
    if board.is_winner('X'):
        print('X wins!')
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            #print('No winner yet')
            break
    
    #if board.no_winner_yet('X'):
        #print('No winner yet')
        #continue



    # check for a tie
    if board.is_tie():
        print('Tie game!')
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break

    # no winner yet
    if board.no_winner_yet('X'):
        print('No winner yet')


    # O goes
    o_column_choice = int(input("\n O - please choose column 1-3. > "))-1
    o_row_choice = int(input("\n O - please choose row 1-3. > "))-1
    # update board with O
    board.update_state(o_row_choice, o_column_choice, 'O')
    
    # O winner
    if board.is_winner('O'):
        print('O wins!') 
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break
    #
 

    # check for a tie
    if board.is_tie():
        print('Tie game!')
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break


#while not True:

