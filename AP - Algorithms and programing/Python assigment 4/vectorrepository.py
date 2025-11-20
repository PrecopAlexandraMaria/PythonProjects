#The repository hold the functions applied on the list of vectors

import matplotlib.pyplot as plt
from myvector import *

class VectorRepository:
    def __init__(self):
        self.__vector_list = []

    def add_vector(self, vector):
        if isinstance(vector, MyVector):
            self.__vector_list.append(vector)
        else:
            raise TypeError("Vector is not valid")

    def get_all_vectors(self):
        return self.__vector_list

    def get_vector_at_index(self, index):
        if index >= len(self.__vector_list) or index < 0:
            raise IndexError('Vector index out of range')
        else:
            return self.__vector_list[index]

    def update_vector_at_index(self, index, vector_update):
        if index >= len(self.__vector_list) or index < 0:
            raise IndexError('Vector index out of range')
        else:
            self.__vector_list[index] = vector_update

    def update_vector_by_name(self, name_id, vector_update):
        for i, vector in enumerate(self.__vector_list):
            if vector.get_name() == name_id:
                self.__vector_list[i] = vector_update
                return
        raise ValueError('Vector name not found')

    def delete_vector_by_index(self, index):
        if index >= len(self.__vector_list) or index < 0:
            raise IndexError('Vector index out of range')
        else:
            self.__vector_list.pop(index)

    def delete_vector_by_name(self, name_id):
        for i, vector in enumerate(self.__vector_list):
            if vector.get_name() == name_id:
                self.__vector_list.pop(i)
                return
        raise ValueError('Vector name not found')

    def plot_points_in_chart_by_type_and_colour(self):
        if not self.__vector_list:
            print("No vectors available to plot.")
            return
        for i, vector in enumerate(self.__vector_list):
            values = vector.get_value_list()
            color = vector.get_colour()
            if vector.get_type() == 1:
                marker = 'o'
            elif vector.get_type() == 2:
                marker = 's'
            elif vector.get_type() == 3:
                marker = 'v'
            else:
                marker = 'd'
            plt.scatter([i] * len(values), values, c=color, marker=marker, label=f"Vector {vector.get_name()}")
        plt.title("Vectors by Index, Type, and Color")
        plt.xlabel("Vector Index")
        plt.ylabel("Values")
        plt.legend()
        plt.show()

    def get_sum_of_elem_in_all_vector(self):
        sum_of_elem = 0
        for vector in self.__vector_list:
            sum_of_elem += vector.sum_of_vector_elements()
        return sum_of_elem

    def delete_all_vectors_by_colour(self, color):
        self.__vector_list = [vector for vector in self.__vector_list if vector.get_colour() != color]

    def update_all_vectors_elem_with_scalar(self, scalar_update):
        for vector in self.__vector_list:
            vector.add_scalar(scalar_update)
