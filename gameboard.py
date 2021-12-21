class GameBoard:
    def __init__(self):
        #create gameboard 2d array
        self.gameboard = []
        for r in range(8):
            row = []
            for column in range(8):
                row.append(".")
            self.gameboard.append(row)