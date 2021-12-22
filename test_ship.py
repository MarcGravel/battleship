import unittest
from ship import Ship


############### UNIT TEST IS INCORRECT###################
class test_ship(unittest.TestCase):
    
    #tests for checking ship direction
    def test_check_direction(self):
        self.assertEqual(Ship.check_direction("h"), "H")
        self.assertEqual(Ship.check_direction("H"), "H")
        self.assertEqual(Ship.check_direction("v"), "V")
        self.assertEqual(Ship.check_direction("V"), "V")
        self.assertEqual(Ship.check_direction("hh"), None)
        self.assertEqual(Ship.check_direction("3"), None)
        self.assertEqual(Ship.check_direction("vH"), None)
        self.assertEqual(Ship.check_direction(" "), None)
        self.assertEqual(Ship.check_direction(""), None)
        self.assertEqual(Ship.check_direction("vvv"), None)
        self.assertEqual(Ship.check_direction(".h"), None)
    
    #tests for horizontal ship placement
    def test_horizontal_ship_placement(self):
        self.assertEqual(Ship.horizontal_ship_placement(6, 1), [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['O', 'O', 'O', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']])
        self.assertEqual(Ship.horizontal_ship_placement(7, 3), [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'O', 'O', 'O', '.', '.', '.']])
        self.assertEqual(Ship.horizontal_ship_placement(1, 0), None)
        self.assertEqual(Ship.horizontal_ship_placement(3, 0), None)
        self.assertEqual(Ship.horizontal_ship_placement(4, 7), None)
        self.assertEqual(Ship.horizontal_ship_placement(6, 7), None)
    
    #tests for vertical ship placement
    def test_vertical_ship_placement(self):
        self.assertEqual(Ship.vertical_ship_placement(1, 0), [['O', '.', '.', '.', '.', '.', '.', '.'], ['O', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['O', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']])
        self.assertEqual(Ship.vertical_ship_placement(5, 3), [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', 'O', '.', '.', '.', '.'], ['.', '.', '.', 'O', '.', '.', '.', '.'], 
                                                                ['.', '.', '.', 'O', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']])
        self.assertEqual(Ship.vertical_ship_placement(0, 3), None)
        self.assertEqual(Ship.vertical_ship_placement(0, 6), None)
        self.assertEqual(Ship.vertical_ship_placement(7, 7), None)
        self.assertEqual(Ship.vertical_ship_placement(7, 2), None)

if __name__ == "__main__":
    unittest.main()