# binary search

def binarySearch(lista, token, l, r):
    if (r-l == 0):
        return "non presente"
    
    mid = (l+r) //2
    print(mid)
    if (lista[mid] == token):
        return f"numero presente alla posizione {mid+1}"
    elif token < lista[mid]:
        return binarySearch(lista, token, l, mid)
    else:
        return binarySearch(lista,token, mid+1, r)


    
if __name__ == '__main__':     

    lista = [i for i in range(1,100)] 

    number = int(input("che numero vuoi cercare?: "))

    print(binarySearch(lista, number, 0, len(lista)))
    
   

 
