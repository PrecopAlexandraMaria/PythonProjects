from domain.plane import *
from domain.passenger import *

def read_plane_list(plane_list):
    plane_list = []
    n = int(input("Enter the number of planes: "))
    for i in range(n):
        name = input("Enter the name of plane: ")
        airline = input("Enter the airline of the plane: ")
        destination = input("Enter the destination of the plane: ")
        seats = int(input("Enter the number of seats on the plane: "))
        passengers = []
        n=int(input("Enter number of passengers: "))
        for i in range(n):
            first_name=input("Enter the first name of passenger: ")
            last_name = input("Enter the last name of passenger: ")
            passport_number = input("Enter the passport number: ")
            passengers.append(Passenger(first_name,last_name,passport_number))
        plane_list.append(Plane(name, airline, destination, seats, passengers))

def menu_message():
    print("Help.",
          "\nThe functions are:",
          "\n1.Add a plane",
          "\n2.Add a passenger",
          "\n3.Remove a plane",
          "\n4.Remove a passenger",
          "\n5.Update a plane",
          "\n6.Update a passenger",
          "\n7.Show all planes",
          "\n8.Show all passengers",
          "\n9.Sort the passengers by last name",
          "\n10.Sort planes according to the number of passengers",
          "\n11.Sort planes according to the number of passengers with the first name starting with a given substring",
          "\n12.Sort planes according to the string obtained by concatenation of the number of passengers in the plane and destination",
          "\n13.Identify planes that have passengers with passport numbers starting with the same 3 letters",
          "\n14.Identify passengers from a given plane for which the first name or last name contains a string given as parameter",
          "\n15.Identify plane/planes where there is a passenger with given name",
          "\n16.Form groups of k passengers from the same plane but with diffrent last names",
          "\n17.Form groups of k planes with the same destination but belonging to diffrent airline companies",
          "\n0.Exit")

def print_menu(planes_list):
    menu_message()
    c = int(input("Enter the exercise: "))
    while (c != 0):
        if c == 1:
            name = input("Enter the name of plane: ")
            airline = input("Enter the airline of the plane: ")
            destination = input("Enter the destination of the plane: ")
            seats = int(input("Enter the number of seats on the plane: "))
            passengers = []
            n = int(input("Enter number of passengers: "))
            for i in range(n):
                first_name = input("Enter the first name of passenger: ")
                last_name = input("Enter the last name of passenger: ")
                passport_number = input("Enter the passport number: ")
                passengers.append(Passenger(first_name, last_name, passport_number))
            planes_list.append(Plane(name, airline, destination, seats, passengers))
            for idx, plane in enumerate(planes_list.get_planes()):
                print(f"{idx}: {plane}")

        elif c == 2:
            for idx, plane in enumerate(planes_list.get_planes()):
                print(f"{idx}: {plane}")

            index = int(input("Enter the index of the plane: "))
            plane = planes_list.get_planes()[index]
            first_name = input("Enter the first name of passenger: ")
            last_name = input("Enter the last name of passenger: ")
            passport_number = input("Enter the passport number: ")
            passenger = Passenger(first_name, last_name, passport_number)
            plane.get_passengers().append(passenger)
            print(f"{plane}")
            for idx, passenger in enumerate(plane.get_passengers()):
                print(f"{idx}: {passenger}")

        elif c == 3:
            for idx, plane in enumerate(planes_list.get_planes()):
                print(f"{idx}: {plane}")

            index = int(input("Enter the index of the plane: "))
            plane = planes_list.get_planes()[index]
            planes_list.remove_plane(plane)
            for idx, plane in enumerate(planes_list.get_planes()):
                print(f"{idx}: {plane}")

        elif c == 4:
            for idx, plane in enumerate(planes_list.get_planes()):
                print('\n')
                print(f"{idx}: {plane}")
                for idxx, passenger in enumerate(plane.get_passengers()):
                    print(f"{idxx}: {passenger}")

            index = int(input("Enter the index of the plane the passenger is in: "))
            indexpass = int(input("Enter the index of the passenger: "))
            plane = planes_list.get_planes()[index]
            passenger = plane.get_passengers()[indexpass]
            planes_list.remove_passenger(passenger, plane)

            print(f"{plane}")
            for idx, passenger in enumerate(plane.get_passengers()):
                print(f"{idx}: {passenger}")

        elif c == 5:
            for idx, plane in enumerate(planes_list.get_planes()):
                print('\n')
                print(f"{idx}: {plane}")
            index = int(input("Enter the index of the plane the passenger is in: "))
            name = input("Enter the name of plane: ")
            airline = input("Enter the airline of the plane: ")
            destination = input("Enter the destination of the plane: ")
            seats = int(input("Enter the number of seats on the plane: "))
            passengers = []
            n = int(input("Enter number of passengers: "))
            for i in range(n):
                first_name = input("Enter the first name of passenger: ")
                last_name = input("Enter the last name of passenger: ")
                passport_number = input("Enter the passport number: ")
                passengers.append(Passenger(first_name, last_name, passport_number))
            planes_list.update_plane(index, name, airline, destination, seats, passengers)
            print(f"{planes_list.get_planes()[index]}")
            for idx, passenger in enumerate(planes_list.get_planes()[index].get_passengers()):
                print(f"{idx}: {passenger}")

        elif c == 6:
            for idx, plane in enumerate(planes_list.get_planes()):
                print('\n')
                print(f"{idx}: {plane}")
                for idxx, passenger in enumerate(plane.get_passengers()):
                    print(f"{idxx}: {passenger}")

            index = int(input("Enter the index of the plane the passenger is in: "))
            indexpass = int(input("Enter the index of the passenger: "))
            first_name = input("Enter the first name of the passenger: ")
            last_name = input("Enter the last name of the passenger: ")
            passport = input("Enter the passport number: ")
            planes_list.update_passenger(index, indexpass, first_name, last_name, passport)
            print(f"{planes_list.get_planes()[index]}")
            for idx, passenger in enumerate(planes_list.get_planes()[index].get_passengers()):
                print(f"{idx}: {passenger}")

        elif c == 7:
            for idx, plane in enumerate(planes_list.get_planes()):
                print(f"{idx}: {plane}")

        elif c == 8:
            for plane in planes_list.get_planes():
                print('\n')
                print(f"{plane}")
                for idx, passenger in enumerate(plane.get_passengers()):
                    print(f"{idx}: {passenger}")

        elif c == 9:
            for idx, plane in enumerate(planes_list.get_planes()):
                print('\n')
                print(f"{idx}: {plane}")
            index = int(input("Enter the index of the plane the passenger is in: "))
            plane = planes_list.get_planes()[index]
            planes_list.sort_passengers_in_plane_by_last_name(plane)
            print(f"{plane}")
            for idx, passenger in enumerate(plane.get_passengers()):
                print(f"{idx}: {passenger}")

        elif c == 10:
            planes_list.sort_planes_by_nr_of_passengers()
            for plane in planes_list.get_planes():
                print('\n')
                print(f"{plane}")

        elif c == 11:
            prefix=input("Enter the prefix: ")
            planes_list.sort_planes_by_number_of_passengers_with_string_in_name(prefix)
            for plane in planes_list.get_planes():
                print('\n')
                print(f"{plane}")

        elif c == 12:
            planes_list.sort_plane_by_nr_passengers_and_destination()
            for plane in planes_list.get_planes():
                print('\n')
                print(f"{plane}")

        elif c == 13:
            list = planes_list.planes_with_passenger_passports_with_same_first_3_letters()
            for plane in planes_list.get_planes():
                if plane in list:
                    print('\n')
                    print(f"{plane}")

        elif c == 14:
            for idx, plane in enumerate(planes_list.get_planes()):
                print('\n')
                print(f"{idx}: {plane}")
            index = int(input("Enter the index of the plane: "))
            string = input("Enter the string within the names of the passengers: ")
            list = planes_list.passengers_from_plane_with_parameter_in_name(index, string)
            print(f"{planes_list.get_planes()[index]}")
            for idx, passenger in enumerate(planes_list.get_planes()[index].get_passengers()):
                if passenger in list:
                    print(f"{idx}: {passenger}")

        elif c == 15:
            for idx, plane in enumerate(planes_list.get_planes()):
                print('\n')
                print(f"{idx}: {plane}")
            index = int(input("Enter the index of the plane: "))
            fname = input("Enter the first name of the passenger: ")
            lname = input("Enter the last name of the passenger: ")
            list = planes_list.plane_with_passenger_name(fname, lname)
            for plane in planes_list.get_planes():
                if plane in list:
                    print('\n')
                    print(f"{plane}")

        elif c == 16:
            k = int(input("Enter the amount of elements of a group: "))
            print(planes_list.passenger_group_from_same_plane_diff_last_name(k))

        elif c == 17:
            k = int(input("Enter the amount of elements of a group: "))
            print(planes_list.plane_group_same_destination_diff_airlines(k))

        print("See menu? \nY for yes, enter to skip question")
        obj=input()
        if obj == "Y" or obj == 'y':
            menu_message()
        c = int(input("Enter the exercise: "))