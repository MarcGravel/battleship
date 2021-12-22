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
                print("That is not a valid input, please enter between 1 and 8")
                print(" ")
        except ValueError:
            print("This is not a valid response, please enter between 1 and 8")
        
    def select_attack_coordinates():
        letterArray = ["A", "B", "C", "D", "E", "F", "G", "H"]
        
        while True:
            p_column = input("Choose a coordinate between A and H: ")
            one_column_upper = p_column.upper()
            if one_column_upper in letterArray:
                column_choice = letterArray.index(one_column_upper)
                break
            else:
                print("That is not a valid input, please enter letter between A and H")
                print(" ")
        while True:
            p_row = input("Choose a coordinate between 1 and 8: ")
            int_return = Player.convert_row_selection(p_row)
            if type(int_return) == int:
                break
        
        return [int_return, column_choice]
