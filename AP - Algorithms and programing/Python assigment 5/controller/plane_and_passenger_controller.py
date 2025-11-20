from domain.plane import Plane
from domain.passenger import Passenger
from infrastructure.plane_and_passenger_repo import PlanesRepo


class PlaneAndPassengerController:
    def __init__(self, repo: PlanesRepo):
        self.repo = repo

    # Plane Management
    def add_plane(self, name, airline, destination, seats, passengers = []):
        plane = Plane(name, airline, destination, seats, passengers)
        self.repo.add_plane(plane)

    def remove_plane(self, plane_index):
        plane = self.repo.get_planes()[plane_index]
        self.repo.remove_plane(plane)

    def update_plane(self, plane_index, name, airline, destination, seats, passengers = []):
        plane = Plane(name, airline, destination, seats, passengers)
        self.repo.get_planes()[plane_index] = plane

    # Passenger Management
    def add_passenger_to_plane(self, first_name, last_name, passport_number, plane_index):
        passenger = Passenger(first_name, last_name, passport_number)
        plane = self.repo.get_planes()[plane_index]
        self.repo.add_passenger(passenger, plane)

    def remove_passenger_from_plane(self, plane_index, passenger_index):
        plane = self.repo.get_planes()[plane_index]
        passenger = plane.get_passengers()[passenger_index]
        self.repo.remove_passenger(passenger, plane)

    def update_passenger_in_plane(self, plane_index, passenger_index, first_name, last_name, passport_number):
        passenger = Passenger(first_name, last_name, passport_number)
        plane = self.repo.get_planes()[plane_index]
        plane.get_passengers()[passenger_index] = passenger

    # Getters
    def get_all_planes(self):
        return self.repo.get_planes()

    def get_all_passengers_in_plane(self, plane_index):
        plane = self.repo.get_planes()[plane_index]
        return plane.get_passengers()

    # Sorting and Searching
    def sort_planes_by_passenger_count(self):
        self.repo.sort_planes_by_nr_of_passengers()

    def sort_planes_by_passenger_count_with_prefix(self, prefix):
        self.repo.sort_planes_by_number_of_passengers_with_string_in_name(prefix)

    def sort_passengers_in_plane(self, plane_index):
        plane = self.repo.get_planes()[plane_index]
        self.repo.sort_passengers_in_plane_by_last_name(plane)

    def sort_planes_by_passenger_count_and_destination(self):
        self.repo.sort_plane_by_nr_passengers_and_destination()

    def find_planes_with_passengers_same_passport_prefix(self):
        return self.repo.planes_with_passenger_passports_with_same_first_3_letters()

    def find_passengers_with_name_substring(self, plane_index, substring):
        return self.repo.passengers_from_plane_with_parameter_in_name(plane_index, substring)

    def find_planes_with_passenger_name(self, first_name, last_name):
        return self.repo.plane_with_passenger_name(first_name, last_name)

    def group_passengers_by_different_last_names(self, k):
        return self.repo.passenger_group_from_same_plane_diff_last_name(k)

    def group_planes_by_same_destination_diff_airlines(self, k):
        return self.repo.plane_group_same_destination_diff_airlines(k)
