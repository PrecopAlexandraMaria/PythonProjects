#Am inlocuit lista cu copia lui aux, salvata si updatata dupa fiecare functie
def undo(list, aux):
    if aux:
        list.clear()
        list.extend(aux.pop())
