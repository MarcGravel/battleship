from gameboard import GameBoard

class Player():
    def __init__(self):
        self.board = GameBoard().gameboard
        
    def convert_row_selection(input):
        try:
            int_row = int(input)
            if int_row >= 1 and int_row <=8:
                int_row = int_row - 1 #minus 1 to account for array zeros
                return int_row
            else:
                print("That is not a valid input")
        except ValueError:
            print("This is not a valid input")
            
    def convert_letter_choice_to_number(col):
        letterArray = ["A", "B", "C", "D", "E", "F", "G", "H"]
        
        one_column_upper = col.upper()
        if one_column_upper in letterArray:
            column_choice = letterArray.index(one_column_upper)
            return column_choice
        else:
            print("That is not a valid input, please enter letter between A and H")
            print(" ")
        
    def select_attack_coordinates():   
        while True:
            p_column = input("Choose a coordinate between A and H: ")
            column = Player.convert_letter_choice_to_number(p_column)
            if column != None:
                break
            
        while True:
            p_row = input("Choose a coordinate between 1 and 8: ")
            row = Player.convert_row_selection(p_row)
            if type(row) == int:
                break
        
        return [row, column]
