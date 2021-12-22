from gameboard import GameBoard
from player import Player

class Ship():
    
    def check_direction(dir):
        upper_direction = dir.upper() #uppercase the input for the function check
                
        if upper_direction == "H" or upper_direction == "V":
            return upper_direction
        else:
            print("That is not a valid input")
            print(" ")
            
    def horizontal_ship_placement(row, column):
        board = GameBoard().gameboard
        
        #if horizontal, column cannot be 0 or 7 at center or ship is out of bounds
        if column != 0 and column != 7:
            #center of ship
            board[row][column] = "O"
            #front and back of ship
            board[row][column - 1] = "O"
            board[row][column + 1] = "O"
            return board
        else: 
            print("Can't place ship here, try again")
            
    def vertical_ship_placement(row, column):
        board = GameBoard().gameboard
        
        #if vertical, row cannot be 0 or 7 at center or ship is out of bounds
        if row != 0 and row != 7:
            #center of ship
            board[row][column] = "O"
            #front and back of ship
            board[row - 1][column] = "O"
            board[row + 1][column] = "O"
            return board
        else: 
            print("Can't place ship here, try again")
    
    def set_ship_coordinates():
        while True:
            while True:
                direction_input = input("Which direction? Horizontal 'H' or Vertical 'V': ")
                direction = Ship.check_direction(direction_input)
                if direction != None:
                    break
                    
            while True: 
                column_input = input("Which Column? (Between A and H): ")
                column = Player.convert_letter_choice_to_number(column_input) #uses same algo as convert row in player class
                if column != None:
                    break
                    
            while True: 
                row_input = input("Which row? (Between 1 and 8): ")
                row = Player.convert_row_selection(row_input) #uses same algo as convert row in player class
                if row != None:
                    break
                    
            if direction == "H":
                board = Ship.horizontal_ship_placement(row, column)
                if board != None:
                    return board
            elif direction == "V":
                board = Ship.vertical_ship_placement(row, column)
                if board != None:
                    return board
            else:
                print("Something went wrong, try again.")