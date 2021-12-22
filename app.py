from player import Player
from ship import Ship

def check_shot_value(value):
    if value == "O":
        print("")
        print("Hit")
        print("")
    elif value == "X":
        print("")
        print("You already Hit here")
        print("")
    else:
        print("")
        print("Miss")
        print("")
        
def check_for_win(board, player):
    #check for destroyed boat
    if not any("O" in b for b in board):
        print(str(player)+" Says: You sunk my battleship!!!")
        print("Press enter to exit")
        return True
    else:
        return False

def play_game():
    player_one = Player()
    player_two = Player()
    
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
        shot_value = player_two.board[p_one_attack[0]][p_one_attack[1]]
        player_two.board[p_one_attack[0]][p_one_attack[1]] = "X"
        
        check_shot_value(shot_value)
        isWin = check_for_win(player_two.board, "Player Two")
        if isWin:
            break
        
        print("PLAYER TWO, Select attack coordinates.")
        p_two_attack = Player.select_attack_coordinates()
        #player two attacks player one
        shot_value = player_one.board[p_two_attack[0]][p_two_attack[1]]
        player_one.board[p_two_attack[0]][p_two_attack[1]] = "X"
        
        check_shot_value(shot_value)
        isWin = check_for_win(player_one.board, "Player One")
        if isWin:
            #hold program on until user follows prompt to press enter to exit
            input()
            break
            
if __name__ == '__main__':
    play_game()