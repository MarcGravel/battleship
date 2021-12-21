from gameboard import GameBoard

class Ship():
    
    def set_ship_coordinates():
        letterArray = ["A", "B", "C", "D", "E", "F", "G", "H"]
        board = GameBoard().gameboard
        
        while True:
        
            while True:
                direction_input = input("Which direction? Horizontal 'H' or Vertical 'V': ")
                upper_direction = direction_input.upper() #uppercase the input for the function check
                
                if upper_direction == "H" or upper_direction == "V":
                    break
                else:
                    print("That is not a valid input, please enter H or V")
                    print(" ")
            
            while True: 
                row_input = input("Which row? (Between 1 and 8): ")
                try:
                    int_row = int(row_input)
                    if int_row >= 1 and int_row <=8:
                        break
                    else:
                        print("That is not a valid input, please enter between 1 and 8")
                        print(" ")
                except ValueError:
                    print("This is not a valid response, please enter between 1 and 8")
                    
            while True: 
                column_input = input("Which Column? (Between A and H): ")
                upper_column = column_input.upper() #uppercase the input for loop check
                
                if upper_column in letterArray:
                    column_choice = letterArray.index(upper_column)
                    break
                else:
                    print("That is not a valid input, please enter letter between A and H")
                    print(" ")
            
            dir = upper_direction
            row = int_row - 1 #remove one here to account for 0 in list 
            column = column_choice #this is already an index value and does not need to -1
            
            if dir == "H":
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
            elif dir == "V":
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
            else:
                print("Something went wrong")