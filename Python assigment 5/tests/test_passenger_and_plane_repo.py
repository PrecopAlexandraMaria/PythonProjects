import unittest
from infrastructure.plane_and_passenger_repo import PlanesRepo
from domain.plane import Plane
from domain.passenger import Passenger


class TestPlanesAndPassengersRepo(unittest.TestCase):
    def setUp(self):
        self.repo = PlanesRepo()

        self.passenger1 = Passenger("Alice", "Smith", "FUS12345")
        self.passenger2 = Passenger("Bob", "Johnson", "MUS67890")
        self.passenger3 = Passenger("Charlie", "Brown", "MUS54321")

        self.plane1 = Plane("Plane A", "Airline X", "Destination Y", 2, [self.passenger1])
        self.plane2 = Plane("Plane B", "Airline Y", "Destination Z", 3, [self.passenger2, self.passenger3])
        self.repo.add_plane(self.plane1)
        self.repo.add_plane(self.plane2)

    def test_add_plane(self):
        new_plane = Plane("Plane C", "Airline Z", "Destination W", 5)
        self.repo.add_plane(new_plane)
        self.assertIn(new_plane, self.repo.get_planes())

    def test_remove_plane(self):
        self.repo.remove_plane(self.plane1)
        self.assertNotIn(self.plane1, self.repo.get_planes())

    def test_remove_nonexistent_plane(self):
        new_plane = Plane("Nonexistent Plane", "Airline X", "Destination Y", 10)
        with self.assertRaises(ValueError):
            self.repo.remove_plane(new_plane)

    def test_update_plane(self):
        self.repo.update_plane(0, "Updated Plane", "Updated Airline", "Updated Destination", 4, passengers=[self.passenger1, self.passenger2, self.passenger3])
        updated_plane = self.repo.get_planes()[0]
        self.assertEqual(updated_plane.get_name(), "Updated Plane")
        self.assertEqual(updated_plane.get_airline(), "Updated Airline")
        self.assertEqual(updated_plane.get_destination(), "Updated Destination")
        self.assertEqual(updated_plane.get_seats(), 4)
        self.assertEqual(updated_plane.get_passengers()[0], self.passenger1)

    def test_add_passenger(self):
        new_passenger = Passenger("David", "Clark", "MUS45678")
        self.repo.add_passenger(new_passenger, self.plane1)
        self.assertIn(new_passenger, self.plane1.get_passengers())

    def test_add_passenger_to_full_plane(self):
        plane = Plane("Plane A", "Airline A", "Destination A", 1, [
            Passenger("Alice", "Smith", "FUS12345")
        ])
        self.repo.add_plane(plane)

        new_passenger = Passenger("Bob", "Johnson", "FUS67890")

        with self.assertRaises(Exception):
            self.repo.add_passenger(new_passenger, plane)

    def test_remove_passenger(self):
        self.repo.remove_passenger(self.passenger1, self.plane1)
        self.assertNotIn(self.passenger1, self.plane1.get_passengers())

    def test_remove_nonexistent_passenger(self):
        new_passenger = Passenger("Nonexistent", "Person", "MUS00000")
        with self.assertRaises(ValueError):
            self.repo.remove_passenger(new_passenger, self.plane1)

    def test_update_passenger(self):
        self.repo.update_passenger(1, 0, "Updated", "Name", "FUS11111")
        updated_passenger = self.plane2.get_passengers()[0]
        self.assertEqual(updated_passenger.get_first_name(), "Updated")
        self.assertEqual(updated_passenger.get_last_name(), "Name")
        self.assertEqual(updated_passenger.get_passport_number(), "FUS11111")

    # Sorting Tests
    def test_sort_planes_by_nr_of_passengers(self):
        self.repo.sort_planes_by_nr_of_passengers()
        sorted_planes = self.repo.get_planes()
        self.assertEqual(sorted_planes[0], self.plane1)  # Plane1 has 1 passenger, Plane2 has 2.

    def test_sort_passengers_in_plane_by_last_name(self):
        passenger4 = Passenger("Adam", "Adams", "FUS12312")
        self.plane2.get_passengers().append(passenger4)
        self.repo.sort_passengers_in_plane_by_last_name(self.plane2)
        sorted_passengers = self.plane2.get_passengers()
        self.assertEqual(sorted_passengers[0].get_last_name(), "Adams")  # Alphabetical order

    def test_sort_planes_by_passenger_count_with_prefix(self):
        passenger4 = Passenger("Alice", "Adams", "MUS33333")
        self.plane2.get_passengers().append(passenger4)
        self.repo.sort_planes_by_number_of_passengers_with_string_in_name("Alice")
        sorted_planes = self.repo.get_planes()
        self.assertEqual(sorted_planes[1], self.plane2)  # Plane2 has more passengers starting with "Alice"

    def test_sort_planes_by_passenger_count_and_destination(self):
        self.repo.sort_plane_by_nr_passengers_and_destination()
        sorted_planes = self.repo.get_planes()
        self.assertEqual(sorted_planes[0].get_destination(), "Destination Y")  # Plane1 has fewer passengers.

    # Search Tests
    def test_planes_with_passenger_passports_with_same_first_3_letters(self):
        result = self.repo.planes_with_passenger_passports_with_same_first_3_letters()
        self.assertIn(self.plane2, result)

    def test_passengers_from_plane_with_parameter_in_name(self):
        result = self.repo.passengers_from_plane_with_parameter_in_name(1, "Charlie")
        self.assertIn(self.passenger3, result)

    def test_plane_with_passenger_name(self):
        result = self.repo.plane_with_passenger_name("Alice", "Smith")
        self.assertIn(self.plane1, result)

    def test_passenger_group_from_same_plane_diff_last_name(self):
        plane = Plane("Plane A", "Airline A", "Destination A", 10, [
            Passenger("Alice", "Smith", "FUS12345"),
            Passenger("Bob", "Johnson", "FUS67890"),
            Passenger("Charlie", "Brown", "FUS54321"),
            Passenger("David", "White", "FUS23456"),
            Passenger("Eve", "Smith", "FUS98765")
        ])
        self.repo.add_plane(plane)

        groups = self.repo.passenger_group_from_same_plane_diff_last_name(2)
        self.assertEqual(len(groups), 2)

    def test_plane_group_same_destination_diff_airlines(self):
        plane1 = Plane("Plane A", "Airline X", "Destination Y", 10)
        plane2 = Plane("Plane B", "Airline Y", "Destination Y", 15)
        plane3 = Plane("Plane C", "Airline Z", "Destination Y", 20)
        self.repo.add_plane(plane1)
        self.repo.add_plane(plane2)
        self.repo.add_plane(plane3)

        groups = self.repo.plane_group_same_destination_diff_airlines(2)
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups[0][0], "Destination Y")
        self.assertEqual(len(groups[0][1]), 2)
        airlines = [plane.get_airline() for plane in groups[0][1]]
        self.assertEqual(len(set(airlines)), 1)


if __name__ == "__main__":
    unittest.main()
