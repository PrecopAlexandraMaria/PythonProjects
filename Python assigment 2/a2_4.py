#am parcurs lungimea de la capetele date si am facut suma
def sum(list, i, j):
    print()
    if i > j:
        a = i
        i = j
        j = a
    if j > len(list) :
        j = len(list)
    if i > len(list) :
        i = len(list)
    s=0
    for k in range(i-1, j):
        s+=list[k]
    print(s)

#am parcurs lungimea de la capetele date si am cautat cmmdc prin impartire
def gcd(list, i, j):
    print()
    if i > j:
        a = i
        i = j
        j = a
    if j > len(list) :
        j = len(list)
    if i > len(list) :
        i = len(list)
    c=list[i-1]
    for k in range(i, j):
        while list[i]!=0:
            r=c%list[i]
            c=list[i]
            list[i]=r
    print(c)

#am parcurs lungimea de la capetele date si am cautat maximul prin comparare
def max(list, i, j):
    print()
    if i > j:
        a = i
        i = j
        j = a
    if j > len(list) :
        j = len(list)
    if i > len(list) :
        i = len(list)
    m=list[i-1]
    for k in range(i, j):
        if list[k]>m:
            m=list[k]
    print(m)