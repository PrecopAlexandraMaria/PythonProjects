#The vector repository gets tested here

import unittest
from vectorrepository import *
from myvector import *

class VectorRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repo = VectorRepository()
        self.vector1 = MyVector('a', 'r', 1, [1])
        self.vector2 = MyVector('b', 'b', 2, [1, 3])
        self.vector3 = MyVector('c', 'r', 3, [1, 2, 3])
        self.repo.add_vector(self.vector1)
        self.repo.add_vector(self.vector2)
        self.repo.add_vector(self.vector3)

    def test_add_vector(self):
        vector4 = MyVector('d', 'm', 3, [5, 8, 3])
        self.repo.add_vector(vector4)
        self.assertIn(vector4, self.repo.get_all_vectors(), "Add vector failed")

    def test_get_all_vectors(self):
        result = self.repo.get_all_vectors()
        self.assertEqual(result, [self.vector1, self.vector2, self.vector3], "Get all vectors failed")

    def test_get_vector_at_index(self):
        result = self.repo.get_vector_at_index(1)
        self.assertEqual(result, self.vector2, "Get vector at index failed")
        with self.assertRaises(IndexError):
            self.repo.get_vector_at_index(10)

    def test_update_vector_at_index(self):
        updated_vector = MyVector('z', 'g', 2, [5, 5])
        self.repo.update_vector_at_index(1, updated_vector)
        self.assertEqual(self.repo.get_vector_at_index(1), updated_vector, "Update vector at index failed")
        with self.assertRaises(IndexError):
            self.repo.update_vector_at_index(10, updated_vector)

    def test_update_vector_by_name(self):
        updated_vector = MyVector('z', 'g', 2, [5, 5])
        self.repo.update_vector_by_name('b', updated_vector)
        self.assertEqual(self.repo.get_vector_at_index(1), updated_vector, "Update vector by name failed")
        with self.assertRaises(ValueError):
            self.repo.update_vector_by_name('unknown', updated_vector)

    def test_delete_vector_by_index(self):
        self.repo.delete_vector_by_index(1)
        self.assertNotIn(self.vector2, self.repo.get_all_vectors(), "Delete vector by index failed")
        with self.assertRaises(IndexError):
            self.repo.delete_vector_by_index(10)

    def test_delete_vector_by_name(self):
        self.repo.delete_vector_by_name('b')
        self.assertNotIn(self.vector2, self.repo.get_all_vectors(), "Delete vector by name failed")
        with self.assertRaises(ValueError):
            self.repo.delete_vector_by_name('unknown')

    def test_delete_all_vectors_by_colour(self):
        self.repo.delete_all_vectors_by_colour('r')
        self.assertNotIn(self.vector1, self.repo.get_all_vectors(), "Delete all vectors by color failed")
        self.assertNotIn(self.vector3, self.repo.get_all_vectors(), "Delete all vectors by color failed")

    def test_get_sum_of_elem_in_all_vector(self):
        result = self.repo.get_sum_of_elem_in_all_vector()
        self.assertEqual(result, 1 + (1 + 3) + (1 + 2 + 3), "Sum of elements in all vectors failed")

    def test_update_all_vectors_elem_with_scalar(self):
        self.repo.update_all_vectors_elem_with_scalar(2)
        self.assertEqual(self.vector1.get_value_list(), [3], "Scalar update failed for vector1")
        self.assertEqual(self.vector2.get_value_list(), [3, 5], "Scalar update failed for vector2")
        self.assertEqual(self.vector3.get_value_list(), [3, 4, 5], "Scalar update failed for vector3")


if __name__ == "__main__":
    unittest.main()