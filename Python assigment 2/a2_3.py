#am parcurs lungimea de la capetele date si am cautat numerele prime prin verificarea fiecarei valori pentru a gasi posibili divizori
def prime(list, i, j):
    print()
    if i > j:
        a = i
        i = j
        j = a
    if j > len(list) :
        j = len(list)
    if i > len(list) :
        i = len(list)
    ok=0
    for k in range(i-1, j):
        d=2
        while d<=list[k]//2:
            if list[k]%d == 0:
                d=list[k]
            d+=1
        if d<list[k] and list[k]>1 or list[k]==2:
            print(list[k], end=" ")
            ok=1
    if ok==0:
        print("Nu exista")

#am parcurs lungimea de la capetele date si am cautat numerele impare
def odd(list, i, j):
    print()
    if i > j:
        a = i
        i = j
        j = a
    if j > len(list) :
        j = len(list)
    if i > len(list) :
        i = len(list)
    ok=0
    for k in range(i-1, j):
        if list[k]%2 != 0:
            print(list[k], end=" ")
            ok=1
    if ok==0:
        print("Nu exista")
