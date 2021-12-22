import unittest
from player import Player

class test_player(unittest.TestCase):
    
    #Tests for selecting attack coordinates
    
    def test_convert_input_to_int_minus_one(self):
        self.assertEqual(Player.convert_row_selection("4"), 3)
        self.assertEqual(Player.convert_row_selection("8"), 7)
        self.assertEqual(Player.convert_row_selection("2"), 1)
        
    def test_convert_input_to_int_out_of_range(self):
        self.assertEqual(Player.convert_row_selection("9"), None)
        self.assertEqual(Player.convert_row_selection("0"), None)
        self.assertEqual(Player.convert_row_selection("12"), None)
    
    def test_convert_input_not_int(self):
        self.assertEqual(Player.convert_row_selection("b"), None)
        self.assertEqual(Player.convert_row_selection("$3"), None)
        self.assertEqual(Player.convert_row_selection(" "), None)
        
        
if __name__ == "__main__":
    unittest.main()