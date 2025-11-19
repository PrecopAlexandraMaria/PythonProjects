#adauga la final valoarea x
def add(list, x):
    list.append(x)


#muta toate elementele de la i+1 cu o pozitie la dreapta si insereaza pe i valoarea x
def insert(list, i, x):
    list.append(list[len(list)-1])
    for j in range(len(list)-1,i,-1):
        list[j]=list[j-1]
    list[i]=x

