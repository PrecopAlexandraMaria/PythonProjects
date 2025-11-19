#Here is the vector class that creates the vectors
#It holds a couple of the functions offered by the program

class MyVector:
    Valid_colours=["r", "g", "b", "y", "m"]
    def __init__(self, name="a", colour="r", type=1, value_list=[]):
        self.__name = name
        if colour in self.Valid_colours:
            self.__colour = colour
        else:
            self.__colour='r'
            raise ValueError(f"Invalid colour, color must be {self.Valid_colours}")
        if type>=1:
            self.__type = type
        elif self.__type < 1:
            raise TypeError("Type must be an integer")
        self.__value_list = value_list

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_colour(self):
        return self.__colour

    def set_colour(self, new_colour):
        if new_colour in self.Valid_colours:
            self.__colour = new_colour
        else:
            self.__colour='r'
            raise ValueError(f"Invalid colour, color must be {self.Valid_colours}")

    def get_type(self):
        return self.__type

    def set_type(self, new_type):
        if new_type >= 1:
            self.__type = new_type

    def get_value_list(self):
        return self.__value_list

    def set_value_list(self, new_value_list):
        self.__value_list = new_value_list

    def add_scalar(self, scalar):
        for i in range(len(self.__value_list)):
            self.__value_list[i] += scalar

    def add_two_vectors(self, vector2):
        vector_sum=[]
        for i in range(len(self.__value_list)):
            vector_sum.append(self.__value_list[i] + vector2.get_value_list()[i])
        return vector_sum

    def subtract_two_vectors(self, vector2):
        vector_subtract=[]
        for i in range(len(self.__value_list)):
            vector_subtract.append(self.__value_list[i] - vector2.get_value_list()[i])
        return vector_subtract

    def multiply_two_vectors(self, vector2):
        vector_product=0
        for i in range(len(self.__value_list)):
            vector_product += self.__value_list[i] * vector2.get_value_list()[i]
        return vector_product

    def sum_of_vector_elements(self):
        sum_elements = 0
        for i in range(len(self.__value_list)):
            sum_elements += self.__value_list[i]
        return sum_elements

    def product_of_vector_elements(self):
        product_elements = 1
        for i in range(len(self.__value_list)):
            product_elements *= self.__value_list[i]
        return product_elements

    def average_of_vector_elements(self):
        sum_of_elements = 0
        for i in range(len(self.__value_list)):
            sum_of_elements += self.__value_list[i]
        avg_elements = sum_of_elements / len(self.__value_list)
        return avg_elements

    def minimum_of_vector_elements(self):
        min=self.__value_list[0]
        for i in range(len(self.__value_list)):
            if self.__value_list[i] < min:
                min = self.__value_list[i]
        return min

    def maximum_of_vector_elements(self):
        max=self.__value_list[0]
        for i in range(len(self.__value_list)):
            if self.__value_list[i] > max:
                max = self.__value_list[i]

    def __repr__(self) -> str:
        return f"Vector(name_id: {self.__name}, colour: {self.__colour}, type: {self.__type}, value_list: {self.__value_list})"

    def __eq__(self, vector) -> bool:
        if not isinstance(vector, MyVector):
            return NotImplemented
        return (
                self.__name == vector.get_name() and
                self.__colour == vector.get_colour() and
                self.__type == vector.get_type() and
                self.__value_list == vector.get_value_list()
                )


if __name__ == "__main__":
    s = MyVector('A', 'r', 2, [1, 2])
    print(repr(s))