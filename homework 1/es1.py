

if __name__ == '__main__':

    lista = input("inserisci una lista di numeri separati da virgola: ")
    
    lista = [ int(element) for element in lista.split(',') ]

    print(lista)