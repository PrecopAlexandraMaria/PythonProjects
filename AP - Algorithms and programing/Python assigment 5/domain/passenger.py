class Passenger:
    def __init__(self, first_name, last_name, passport_number):
        self.__first_name = first_name
        self.__last_name = last_name

        if len(passport_number) != 8 :
            self.__passport_number = ""
            raise ValueError("Passport number must be 8 characters")
        elif passport_number[0] not in ['M', 'F'] :
            self.__passport_number = ""
            raise ValueError("Passport must start with M or F")
        elif not passport_number[0:2].isalpha() :
            self.__passport_number = ""
            raise ValueError("Passport number must start with 3 letters from A or Z")
        elif not passport_number[3:].isdigit() :
            self.__passport_number = ""
            raise ValueError("Passport number must have digits as the last 5 characters")

        self.__passport_number = passport_number

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} ({self.__passport_number})"

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_passport_number(self):
        return self.__passport_number

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_passport_number(self, passport_number):
        self.__passport_number = passport_number