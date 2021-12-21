from unittest import mock
from unittest import TestCase
import unittest
from ship import Ship

############### UNIT TEST IS INCORRECT###################
class test_set_ship_coordinates(TestCase):
    @mock.patch("ship.Ship.set_ship_coordinates.input", create=True)
    def test_set_coordinates_correct(self, mocked_input):
        mocked_input.side_effect = ["h", '2', 'c']
        result = Ship.set_ship_coordinates()
        self.assertEqual(result, {'h', 1, 2})
        
if __name__ == "__main__":
    unittest.main()