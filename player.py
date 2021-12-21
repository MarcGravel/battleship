from gameboard import GameBoard

class Player():
    def __init__(self):
        self.board = GameBoard().gameboard
        
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
            try:
                int_row = int(p_row)
                if int_row >= 1 and int_row <=8:
                    int_row = int_row - 1 #minus 1 to account for array zeros
                    break
                else:
                    print("That is not a valid input, please enter between 1 and 8")
                    print(" ")
            except ValueError:
                print("This is not a valid response, please enter between 1 and 8")
        
        return [int_row, column_choice]
