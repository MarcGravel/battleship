import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    
    #Tests for selecting attack coordinates
    
    def test_convert_row_selection_success(self):
        self.assertEqual(Player.convert_row_selection("8"), 7)
        self.assertEqual(Player.convert_row_selection("2"), 1)
        
    def test_convert_row_selection_fail(self):
        self.assertEqual(Player.convert_row_selection("12"), None)
        self.assertEqual(Player.convert_row_selection("b"), None)
        self.assertEqual(Player.convert_row_selection(" "), None)
        
    def test_convert_letter_choice_to_number_success(self):
        self.assertEqual(Player.convert_letter_choice_to_number("a"), 0)
        self.assertEqual(Player.convert_letter_choice_to_number("C"), 2)
    
    def test_convert_letter_choice_to_number_fail(self):
        self.assertEqual(Player.convert_letter_choice_to_number("3"), None)
        self.assertEqual(Player.convert_letter_choice_to_number("m"), None)
        
if __name__ == "__main__":
    unittest.main()