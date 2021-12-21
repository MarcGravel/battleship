from player import Player
from ship import Ship

def play_game():
    player_one = Player()
    player_two = Player()
    letterArray = ["A", "B", "C", "D", "E", "F", "G", "H"]
    
    print("-------------------")
    print("Welcome to BattleShip, 2-player mode.")
    print("Ships have a length of 3")
    print("-------------------")
    
    print("PLAYER ONE, Please choose the center coordinate for your ship")
    player_one.board = Ship.set_ship_coordinates()
    print(" ")
    
    print("PLAYER TWO, Please choose the center coordinate for your ship")
    player_two.board = Ship.set_ship_coordinates()
    print(" ")
    
    while True:
        print("PLAYER ONE, Select attack coordinates.")
        p_one_attack = Player.select_attack_coordinates()
        #player one attacks player two
        player_two.board[p_one_attack[0]][p_one_attack[1]] = "X"
        
        #check for destroyed boat
        if not any("O" in b for b in player_two.board):
            print("Player Two Says: You sunk my battleship")
            print("")
            print("Press any key to exit")
            input()
        
        print("PLAYER TWO, Select attack coordinates.")
        p_two_attack = Player.select_attack_coordinates()
        #player two attacks player one
        player_one.board[p_two_attack[0]][p_two_attack[1]] = "X"
        
        #check for destroyed boat
        if not any("O" in b for b in player_one.board):
            print("Player Two Says: You sunk my battleship")
            print("")
            print("Press any key to exit")
            input()
            
if __name__ == '__main__':
    play_game()