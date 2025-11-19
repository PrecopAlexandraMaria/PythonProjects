import unittest
from domain.plane import Plane
from domain.passenger import Passenger


class TestPlane(unittest.TestCase):
    def test_create_plane(self):
        plane = Plane("Boeing 737", "AirlineA", "CityA", 150)
        self.assertEqual(plane.get_name(), "Boeing 737")
        self.assertEqual(plane.get_airline(), "AirlineA")
        self.assertEqual(plane.get_destination(), "CityA")
        self.assertEqual(plane.get_seats(), 150)
        self.assertEqual(len(plane.get_passengers()), 1)

    def test_add_passenger(self):
        plane = Plane("Boeing 737", "AirlineA", "CityA", 2)
        passenger = Passenger("Alice", "Smith", "FUS12345")
        plane.get_passengers().append(passenger)
        self.assertEqual(len(plane.get_passengers()), 1)
        self.assertEqual(plane.get_passengers()[0].get_first_name(), "Alice")
