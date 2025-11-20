from domain.passenger import Passenger
from domain.plane import *
from controller.plane_and_passenger_controller import *
from infrastructure.plane_and_passenger_repo import PlanesRepo
from ui.library_ui import *

if __name__ == '__main__':
    p1_1 = Passenger('Ana', 'Popescu', 'FRO73010')
    p2_1 = Passenger('Beatrice', 'Chivu', 'FMK78345')
    p3_1 = Passenger('Ana-Maria', 'Rancu', 'FNU72395')
    p4_1 = Passenger('Cornel', 'Manulescu', 'MOL01234')

    p1_2 = Passenger('Andrei', 'Pop', 'MRO73010')
    p2_2 = Passenger('Olivia', 'Chivu', 'FMK72365')
    p3_2 = Passenger('Constantin', 'Pop', 'MQP93649')
    p4_2 = Passenger('Olivia', 'Chivu', 'MMK92614')

    p1_3 = Passenger('Bernard', 'Nicu', 'MNO93653')
    p2_3 = Passenger('Olesia', 'Ranca', 'FAI78346')
    p3_3 = Passenger('Anda-Maria', 'Stan', 'FAI92483')
    p4_3 = Passenger('Alexandra-Maria', 'Precop', 'FSV01304')

    plane_1 = Plane('FlyHigh', 'WizzAir', 'Maldive', 33, [p1_1, p2_1, p3_1, p4_1])
    plane_2 = Plane('Cloud', 'BeesAirlines', 'Hawai', 50, [p1_2, p2_2, p3_2, p4_2])
    plane_3 = Plane('Powerpuffgrlz', 'BadBAirlines', 'Olanda', 40, [p1_3, p2_3, p3_3, p4_3])

    planes_list = PlanesRepo()
    print("Use already implemented planes list:1 \nUser input plane list:2")
    ch=int(input("Enter your choice: "))
    if ch==1:
        planes_list.add_plane(plane_1)
        planes_list.add_plane(plane_2)
        planes_list.add_plane(plane_3)
    elif ch==2:
        read_plane_list(planes_list)
    else:
        print('User input error. The test plane list will be used')
        planes_list.add_plane(plane_1)
        planes_list.add_plane(plane_2)
        planes_list.add_plane(plane_3)

    print_menu(planes_list)
