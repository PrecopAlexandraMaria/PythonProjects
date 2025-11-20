from unittest import result

from domain.plane import *
from domain.passenger import *

class PlanesRepo:
    def __init__(self):
        self.__planes = []

    def get_passengers(self, plane):
        return plane.get_passengers()

    def add_passenger(self, passenger, plane):
        if len(plane.get_passengers()) >= plane.get_seats():
            raise Exception("Not enough seats available")  # Exception is raised here
        plane.get_passengers().append(passenger)

    def remove_passenger(self, remove_passenger, plane):
        removed = False
        for i, passenger in enumerate(plane.get_passengers()):
            if passenger == remove_passenger:
                plane.get_passengers().pop(i)
                removed = True
                break
        if not removed:
            raise ValueError('Passenger not found')

    def update_passenger(self, index, indexpass, first_name, last_name, passport):
        self.__planes[index].get_passengers()[indexpass] = Passenger(first_name, last_name, passport)

    def get_planes(self):
        return self.__planes

    def add_plane(self, plane):
        self.__planes.append(plane)

    def remove_plane(self, remove_plane):
        removed = False
        for i, plane in enumerate(self.__planes):
            if plane == remove_plane:
                self.__planes.pop(i)
                removed = True
        if not removed:
            raise ValueError('Plane name not found')

    def update_plane(self, index, name, airline, destination, seats, passengers):
        self.__planes[index] = Plane(name, airline, destination, seats, passengers)

# 3
# we first sort by the last name, if its the same we check the first name
    def sort_passengers_in_plane_by_last_name(self, sorted_plane):
        for plane in self.__planes:
            if plane == sorted_plane:
                passengers = plane.get_passengers()
                sorted = False
                while sorted == False:
                    sorted = True
                    for i in range(len(passengers) - 1):
                        if passengers[i].get_last_name() > passengers[i + 1].get_last_name():
                            sorted = False
                            temp = passengers[i]
                            passengers[i] = passengers[i + 1]
                            passengers[i + 1] = temp
                        if passengers[i].get_last_name() == passengers[i + 1].get_last_name():
                            if passengers[i].get_first_name() > passengers[i + 1].get_first_name():
                                sorted = False
                                temp = passengers[i]
                                passengers[i] = passengers[i + 1]
                                passengers[i + 1] = temp

# 4
# Create a list with the number of passengers for each plane then sort them at the same time
    def sort_planes_by_nr_of_passengers(self):
        passengers_in_plane = []
        for plane in self.__planes:
            passengers_in_plane.append(len(plane.get_passengers()))
        print(passengers_in_plane)
        sorted = False
        while sorted == False:
            sorted = True
            for i in range(len(passengers_in_plane) - 1):
                if passengers_in_plane[i] > passengers_in_plane[i + 1]:
                    sorted = False
                    temp = passengers_in_plane[i]
                    passengers_in_plane[i] = passengers_in_plane[i + 1]
                    passengers_in_plane[i + 1] = temp
                    temp = self.__planes[i]
                    self.__planes[i] = self.__planes[i + 1]
                    self.__planes[i + 1] = temp

# 5
# First we create a list containing the number of passengers with the string in the name, its elements on the same index as their respective planes. Then we sort them at the same time
    def sort_planes_by_number_of_passengers_with_string_in_name(self, prefix):
        planes_with_prefix = []
        for plane in self.__planes:
            nr = 0
            for passenger in plane.get_passengers():
                if passenger.get_first_name().find(prefix) == 0:
                    nr += 1
            planes_with_prefix.append(nr)
        sorted = False
        while sorted == False:
            sorted = True
            for i in range(len(planes_with_prefix) - 1):
                if planes_with_prefix[i] > planes_with_prefix[i + 1]:
                    sorted = False
                    temp = planes_with_prefix[i]
                    planes_with_prefix[i] = planes_with_prefix[i + 1]
                    planes_with_prefix[i + 1] = temp
                    temp = self.__planes[i]
                    self.__planes[i] = self.__planes[i + 1]
                    self.__planes[i + 1] = temp

# 6
# We save in a list all of the concatenations of the number of passengers and destination then sort it at the same time with the planes with the same indexes
    def sort_plane_by_nr_passengers_and_destination(self):
        passengers_in_plane = []
        for plane in self.__planes:
            passengers_in_plane.append(str(len(plane.get_passengers())) + plane.get_destination())
        sorted = False
        while sorted == False:
            sorted = True
            for i in range(len(passengers_in_plane) - 1):
                if passengers_in_plane[i] > passengers_in_plane[i + 1]:
                    sorted = False
                    temp = passengers_in_plane[i]
                    passengers_in_plane[i] = passengers_in_plane[i + 1]
                    passengers_in_plane[i + 1] = temp
                    temp = self.__planes[i]
                    self.__planes[i] = self.__planes[i + 1]
                    self.__planes[i + 1] = temp

# 7
# We go through every plane and check for every passport number if the ones after if have the same 3 letters at the beginnig, if yes we stop searching in that plane and add it to the list
    def planes_with_passenger_passports_with_same_first_3_letters(self):
        passengers_in_plane = []
        for i in range(0, len(self.__planes)):
            found = False
            for j in range(0, len(self.__planes[i].get_passengers())):
                passport_letters=self.__planes[i].get_passengers()[j].get_passport_number()[:3]
                for h in range(j+1, len(self.__planes[i].get_passengers())):
                    if self.__planes[i].get_passengers()[h].get_passport_number()[:3] == passport_letters:
                        passengers_in_plane.append(self.__planes[i])
                        found = True
                        break
                if found:
                    break
        return passengers_in_plane

# 8
# We get the index of the plane from the user and check for either of their names to contain the string
    def passengers_from_plane_with_parameter_in_name(self, plane_index, string):
        passengers_in_plane = []
        for passenger in self.__planes[plane_index].get_passengers():
            if string in passenger.get_first_name() or string in passenger.get_last_name():
                passengers_in_plane.append(passenger)
        return passengers_in_plane

# 9
# We check every passenger in every plane for the name, if it has the same name we add the plane to a list to save it
    def plane_with_passenger_name(self, fname, lname):
        plane_list = []
        for plane in self.__planes:
            for passenger in plane.get_passengers():
                if passenger.get_first_name() == fname and passenger.get_last_name() == lname:
                    plane_list.append(plane)
        return plane_list

# 10
# We group passengers by their last name for each plane and then identify the ones with unique name, finally we form the groups from those with diffrent last names
    def passenger_group_from_same_plane_diff_last_name(self, k):
        result = []

        for plane in self.__planes:
            last_name_groups = {}
            for passenger in plane.get_passengers():
                last_name = passenger.get_last_name()
                if last_name not in last_name_groups:
                    last_name_groups[last_name] = []
                last_name_groups[last_name].append(passenger)

            unique_last_name_passengers = [
                passengers[0] for passengers in last_name_groups.values() if len(passengers) == 1
            ]

            for i in range(0, len(unique_last_name_passengers), k):
                group = unique_last_name_passengers[i:i + k]
                if len(group) == k:
                    result.append((plane.get_name(), group))

        return result
# 11
# First we group by destination, within each destination, group planes by airline to ensure they don't belong to the same one, afterwards we form the k groups
    def plane_group_same_destination_diff_airlines(self, k):
        result = []

        destination_groups = {}
        for plane in self.__planes:
            destination = plane.get_destination()
            if destination not in destination_groups:
                destination_groups[destination] = []
            destination_groups[destination].append(plane)

        for destination, planes_at_destination in destination_groups.items():
            airline_groups = {}
            for plane in planes_at_destination:
                airline = plane.get_airline()
                if airline not in airline_groups:
                    airline_groups[airline] = []
                airline_groups[airline].append(plane)

            unique_airline_planes = [
                plane for planes in airline_groups.values() for plane in planes
            ]

            for i in range(0, len(unique_airline_planes), k):
                group = unique_airline_planes[i:i + k]
                if len(group) == k:
                    result.append((destination, group))

        return result