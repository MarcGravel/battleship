import unittest
from app import check_for_win, check_shot_value

class test_app(unittest.TestCase):
    
    #Tests for checking shot values
    def test_shot_hit_or_miss(self):
        self.assertEqual(check_shot_value("O"), print("Hit"))
        self.assertEqual(check_shot_value("X"), print("You already Hit here"))
        self.assertEqual(check_shot_value(" "), print("Miss"))
        self.assertEqual(check_shot_value(""), print("Miss"))
        
    #Tests for checking if player win
    def test_check_for_win (self):
        self.assertEqual(check_for_win([["-","-","-","-"],["-","-","X"], ["X","-","X"]], "Player Two"), True)
        self.assertEqual(check_for_win([["-","-","-","-"],["-","-","-","-"], ["-","-","-","-"]], "Player Two"), True)
        self.assertEqual(check_for_win([["-","-","-","-"],["O","X","X"], ["X","-","X"]], "Player Two"), False)
        self.assertEqual(check_for_win([["-","O","O","O"],["-","-","x"], ["x","x","x"]], "Player Two"), False)
        
if __name__ == "__main__":
    unittest.main()