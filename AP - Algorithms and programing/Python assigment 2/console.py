from  a2_1 import add, insert
from a2_2 import remove, removeft, replace
from a2_3 import prime, odd
from a2_4 import sum, gcd, max
from a2_5 import filter_prime, filter_negative
from a2_6 import undo

lg = int(input("Enter the length of the list you want to work on: "))
list=[]
print('Enter the elements of the list: ')
for g in range(0, lg):
    a = int(input())
    list.append(a)
aux=[]

def start():
    global aux, list
    print('Possible operations:add, insert, remove, removeft, replace, prime, odd, sum, gcd, max, filter_prime, filter_negative, undo')
    print('To end the program, input "exit"')
    c=input('Option: ')
    while c!='exit':
        if(c=='add'):
            x = int(input("Enter a number: "))
            aux.append(list.copy())
            add(list, x)
            print(list)

        if(c=='insert'):
            i = int(input("Enter index: "))
            x = int(input("Enter value: "))
            aux.append(list.copy())
            insert(list, i, x)
            print(list)

        if(c=='remove'):
            x = int(input("Enter a number: "))
            aux.append(list.copy())
            remove(list, x)
            print(list)

        if(c=='removeft'):
            i = int(input("Enter from: "))
            j = int(input("Enter to: "))
            aux.append(list.copy())
            removeft(list, i, j)
            print(list)

        if(c=='replace'):
            n = int(input("Enter the length of the first set: "))
            m = int(input("Enter the length of the new set: "))
            ins=[]
            fs=[]
            print('First list: ')
            for k in range (0, n):
                a=int(input())
                ins.append(a)
            print('Final list: ')
            for l in range (0 ,m):
                a=int(input())
                fs.append(a)
            aux.append(list.copy())
            replace(list, ins, fs)

        if(c=='prime'):
            i = int(input("Enter from: "))
            j = int(input("Enter to: "))
            aux.append(list.copy())
            prime(list, i, j)
            print()

        if(c=='odd'):
            i = int(input("Enter from: "))
            j = int(input("Enter to: "))
            aux.append(list.copy())
            odd(list, i, j)
            print()

        if(c=='sum'):
            i = int(input("Enter from: "))
            j = int(input("Enter to: "))
            aux.append(list.copy())
            sum(list, i, j)
        print()

        if(c=='gcd'):
            i = int(input("Enter from: "))
            j = int(input("Enter to: "))
            aux.append(list.copy())
            gcd(list, i,j)
            print()

        if(c=='max'):
            i = int(input("Enter from: "))
            j = int(input("Enter to: "))
            aux.append(list.copy())
            max(list, i, j)
            print()

        if(c=='filter_prime'):
            aux.append(list.copy())
            filter_prime(list)
            print(list)

        if(c=='filter_negative'):
            aux.append(list.copy())
            filter_negative(list)
            print(list)

        if(c=='undo'):
            undo(list, aux)
            print(list)
        print('Possible operations:add, insert, remove, removeft, replace, prime, odd, sum, gcd, max, filter_prime, filter_negative, undo')
        print('To end the program, input "exit"')
        c=input('Option: ')
