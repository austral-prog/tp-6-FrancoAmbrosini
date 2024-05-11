def remove_elements(lista):
    if len(lista) >=6:
        del lista[4:6]
        del lista[0]
        return lista
    elif len(lista) ==5:
        del lista[4]
        del lista[0]
        print(lista)
    elif len (lista) ==0:
        return lista
    else:
        del lista[0]
        return lista




def add_elements(lista):
    lista.insert(0,'Pink')
    lista.append('Yellow')
    return lista

def is_empty(lista):
    if lista==[]:
        return True
    else:
        return False



def check_lists(lista1,lista2):
    if len(lista1)>=3 and len(lista2)>=3:
        if lista1[2] == lista2[2]:
            return True
        else:
            return False
    else:
        return False


def list_of_lists(lista):
    if len(lista[0]) >= 2:
        lista1 = lista[0][:2]
    else:
        lista1 = lista[0][:]
    if len(lista[1]) >= 4:
        lista2 = lista[1][1: 4]
    else:
        lista2 = lista[1][1:]
    if len(lista[2]) >= 2:
        lista3 = lista[2][-2:]
    else:
        lista3 = lista[2][:]
    lista[0] = lista1
    lista[1] = lista2
    lista[2] = lista3
    return lista
