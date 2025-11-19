#The vector class gets tested here

from myvector import *
import unittest

class VectorTest(unittest.TestCase):
    def test_vector(self):
        vector = MyVector('new_name', 'm', 2, [1,2])
        self.assertEqual(vector.get_name(), 'new_name', "name check failed")
        self.assertEqual(vector.get_colour(), 'm', "colour check failed")
        self.assertEqual(vector.get_type(), 2, "type check failed")
        self.assertTrue(isinstance(vector.get_value_list(), list), "values check failed")

    def test_set_colour(self):
        vector = MyVector('new_name', 'm', 2, [1,2])

        self.assertEqual(vector.get_colour(), 'm', 'colour check failed')
        vector.set_colour('y')
        self.assertEqual(vector.get_colour(), 'y', 'type check failed')

    def test_set_type(self):
        vector = MyVector('new_name', 'm', 2, [1,2])
        self.assertEqual(vector.get_type(), 2, "type check failed")
        vector.set_type(3)
        self.assertEqual(vector.get_type(), 3, 'type check failed')

if __name__ == "__main__":
    unittest.main()