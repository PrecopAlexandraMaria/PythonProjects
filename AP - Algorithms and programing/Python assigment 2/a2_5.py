#am parcurs si sters elementele care nu sunt prime
def filter_prime(list):
    i=0
    while i<len(list):
        if(list[i]<2):
            list.pop(i)
        else:
            d=2
            ok=1
            while d<=list[i]//2:
                if list[i]%d == 0:
                    ok=0
                    break
                d+=1
            if ok==0:
                list.pop(i)
            else:
                i+=1

#am parcurs si sters elementele >=0
def filter_negative(list):
    i=0
    while i<len(list):
        if(list[i]>=0):
            list.pop(i)
            i-=1
        i+=1