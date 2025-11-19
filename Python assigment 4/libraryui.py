#The library. The user chooses the exercise by inputting an option c, from 1->9, 17, 21 to trigger the function and 0 to end the program.
#Here is also the function to create the vector list

from vectorrepository import *
from myvector import *



def read_vector_list(vec_list):
    vec_list = []
    n = int(input("Enter the number of vectors: "))
    for i in range(n):
        name = input("Enter the name of vector: ")
        color = input("Enter the colour of the vector: ")
        type = int(input("Enter the type of vector: "))
        values = []
        for i in range(type):
            x=int(input("Enter a value: "))
            values.append(x)
        vec_list.append(MyVector(name, color, type, values))

def menu_message():
    print("Help.",
          "\nThe functions are:",
          "\n1.Add a vector",
          "\n2.Get all vectors",
          "\n3.Get a vector at a given index",
          "\n4.Update a vector at a given index",
          "\n5.Update a vector of a given name_id",
          "\n6.Delete vector by index",
          "\n7.Delete vector by name_id",
          "\n8.Plot all vectors in a chart based on colour and type",
          "\n9.Get the sum of elements of all vectors.",
          "\n17.Delete all vectors by colour.",
          "\n21.Update all vectors by a given scalar.",
          "\n0.Exit")

def print_menu(vec_list):
    menu_message()
    c = int(input("Enter the exercise: "))
    while (c != 0):
        if c == 1:
            name = input("Enter the name of vector: ")
            color = input("Enter the colour of the vector: ")
            type = int(input("Enter the type of vector: "))
            values = []
            for i in range(type):
                x = int(input("Enter a value: "))
                values.append(x)
            new_vector = MyVector(name, color, type, values)
            vec_list.add_vector(new_vector)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 2:
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 3:
            index = int(input("Enter the index of vector: "))
            vec_list.get_vector_at_index(index)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 4:
            index = int(input("Enter the index of vector: "))
            name = input("Enter the name of vector: ")
            color = input("Enter the colour of the vector: ")
            type = int(input("Enter the type of vector: "))
            values = []
            for i in range(type):
                x = int(input("Enter a value: "))
                values.append(x)
            update = MyVector(name, color, type, values)
            vec_list.update_vector_at_index(index, update)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 5:
            name = input("Enter the name of vector: ")
            new_name=input("Enter the new name of vector: ")
            color = input("Enter the colour of the vector: ")
            type = int(input("Enter the type of vector: "))
            values = []
            for i in range(type):
                x = int(input("Enter a value: "))
                values.append(x)
            update = MyVector(new_name, color, type, values)
            vec_list.update_vector_by_name(name, update)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 6:
            index = int(input("Enter the index of vector: "))
            vec_list.delete_vector_by_index(index)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 7:
            name = input("Enter the name of vector: ")
            vec_list.delete_vector_by_name(name)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 8:
            vec_list.plot_points_in_chart_by_type_and_colour()
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 9:
            print(vec_list.get_sum_of_elem_in_all_vector())

        elif c == 17:
            color=input("Enter the color of the vector: ")
            vec_list.delete_all_vectors_by_colour(color)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        elif c == 21:
            scalar=int(input("Enter the scalar: "))
            vec_list.update_all_vectors_elem_with_scalar(scalar)
            for idx, vector in enumerate(vec_list.get_all_vectors()):
                print(f"{idx}: {vector}")

        print("See menu? \nY for yes, enter to skip question")
        obj=input()
        if obj == "Y" or obj == 'y':
            menu_message()
        c = int(input("Enter the exercise: "))
