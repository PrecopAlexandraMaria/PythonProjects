import unittest
from domain.passenger import Passenger


class TestPassenger(unittest.TestCase):
    def test_create_valid_passenger(self):
        passenger = Passenger("John", "Doe", "MUS12345")
        self.assertEqual(passenger.get_first_name(), "John")
        self.assertEqual(passenger.get_last_name(), "Doe")
        self.assertEqual(passenger.get_passport_number(), "MUS12345")

    def test_invalid_passport_length(self):
        with self.assertRaises(ValueError):
            Passenger("John", "Doe", "1234567")

    def test_invalid_passport_prefix(self):
        with self.assertRaises(ValueError):
            Passenger("John", "Doe", "12312345")

    def test_passport_number_with_wrong_digits(self):
        with self.assertRaises(ValueError):
            Passenger("John", "Doe", "FAE12A34")

    def test_setters(self):
        passenger = Passenger("John", "Doe", "MUS12345")
        passenger.set_first_name("Jane")
        passenger.set_last_name("Smith")
        passenger.set_passport_number("FUS67890")
        self.assertEqual(passenger.get_first_name(), "Jane")
        self.assertEqual(passenger.get_last_name(), "Smith")
        self.assertEqual(passenger.get_passport_number(), "FUS67890")
