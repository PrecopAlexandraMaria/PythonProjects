#sterge elementul dupa ce il gaseste in sir
def remove(list, i):
    for j in range(i, len(list)-1):
        list[j] = list[j + 1]
    list.pop()

#sterge elementele de la i la j
def removeft(list, i ,j):
    if i > j:
        a = i
        i = j
        j = a
    if j > len(list):
        j = len(list)
    if i > len(list):
        i = len(list)
    while(j!=i):
        del(list[i])
        j-=1

#cauta un sir din lista care este egal cu x si sterge elementele subsirului, dupa care le adauga pe cele ale lui y
def replace(list, x, y):
    v=len(x)
    i=0
    while i<=len(list)-v:
        ok=1
        for j in range(v):
            if list[i+j]!=x[j]:
                ok=0
                break
        if ok==1:
            for k in range(0, v):
                list.pop(i)
            for j in range(len(y)):
                list.insert(i+j, y[j])
            i+=len(y)
        else:
            i+=1
    print(list)

