#The main where the program is ran.
#User has the option to choose to work on a given set of vectors or to implement one themselves.
#The libraryui gets triggered here.

from myvector import *
from libraryui import *
from vectorrepository import *
from vectorrepository import VectorRepository

if __name__ == '__main__':
    v1 = MyVector('a', 'r', 1, [1])
    v2 = MyVector('b', 'b', 2, [1, 3])
    v3 = MyVector('c', 'r', 3, [1, 2, 3])
    v4 = MyVector('d', 'm', 3, [5, 8, 3])

    vec_list = VectorRepository()
    print("Use already implemented vector list:1 \nUser input vector list:2")
    ch=int(input("Enter your choice: "))
    if ch==1:
        vec_list.add_vector(v1)
        vec_list.add_vector(v2)
        vec_list.add_vector(v3)
        vec_list.add_vector(v4)
    elif ch==2:
        read_vector_list(vec_list)
    else:
        print('User input error. The test vector list will be used')
        vec_list.add_vector(v1)
        vec_list.add_vector(v2)
        vec_list.add_vector(v3)
        vec_list.add_vector(v4)

    print_menu(vec_list)

