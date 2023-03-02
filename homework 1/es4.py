# binary search
# es 4

def binarySearch(list):

    l = len(list)
    print(list)
    if (len(list) == 1):
        if (list[0] == number):
            return "trovato"
        else:
            return "non trovato"

    if ( l % 2 != 0):
        cand = int(l/2) + 1
        if (list[cand-1] == number):
            return "trovato"
        elif (list[cand-1] > number):
            return binarySearch(list[0:cand-1])
        elif (list[cand-1] < number):
            return binarySearch(list[cand:])
    
    if ( l % 2 == 0):
        cand = int(l/2) 

        if (list[cand-1] == number):
            return "trovato"
        elif (list[cand-1] > number):
            return  binarySearch(list[0:cand-1])
        else:
            return binarySearch(list[cand:])

    


   
if __name__ == '__main__':     

    lista = [i for i in range(1,100)] 

    number = int(input("che numero vuoi cercare?: "))
    
    print(f"il numero da te cercato si trova alla posizione: { binarySearch(lista)}")

 
