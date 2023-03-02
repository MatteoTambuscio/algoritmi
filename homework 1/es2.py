
def bubbleSort(lista):

    l = len(lista)
    
    stop = True

    for i in range(0, l-1):
        if (lista[i+1] < lista[i]):
            
            lista[i+1], lista[i] = lista[i], lista[i+1] 

            stop = False
    
    if not stop:
        return bubbleSort(lista)
    else:
        return lista
    
         

        
if __name__ == '__main__':

    lista = input("inserisci una lista di numeri separati da virgola: ")
    
    lista = [ int(element) for element in lista.split(',') ]
   
    lista = bubbleSort(lista)
    print(lista)