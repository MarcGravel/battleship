from player import Player

def play_game():
    player_one = Player()
    player_two = Player()
    
    print("-------------------")
    print("Welcome to BattleShip, 2-player mode.")
    print("Ships have a length of 3")
    print("-------------------")
    
    print("Player One, Please choose the center coordinate for your ship")
    print(" ")
    player_one.board = Player.set_ship_coordinates()
    print(player_one.board)
    
    
if __name__ == '__main__':
    play_game()