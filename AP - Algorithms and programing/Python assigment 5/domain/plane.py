class Plane:
    def __init__(self, name, airline, destination, seats, passengers = []):
        self.__name = name
        self.__airline = airline
        self.__destination = destination
        if seats <= 0:
            raise ValueError("Seats must be greater than 0")
        self.__seats = seats
        self.__passengers = passengers  # List to hold Passenger objects

    def __str__(self):
        return f"Plane {self.__name} ({self.__airline}) to {self.__destination}, Seats: {self.__seats}, Passengers: {len(self.__passengers)}"

    def get_name(self):
        return self.__name

    def get_airline(self):
        return self.__airline

    def get_destination(self):
        return self.__destination

    def get_seats(self):
        return self.__seats

    def get_passengers(self):
        return self.__passengers

    def set_name(self, name):
        self.__name = name

    def set_airline(self, airline):
        self.__airline = airline

    def set_destination(self, destination):
        self.__destination = destination

    def set_seats(self, seats):
        self.__seats = seats

    def set_passengers(self, passengers):
        self.__passengers = passengers