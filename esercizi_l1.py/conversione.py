def conversione(lista):
    lista_parole=["zero","uno","due","tre","quattro"]
    lista_stringhe=[lista_parole[numero] for numero in lista]
    return lista_stringhe


lista=[1,1,1,3,4,3,3]
print(conversione(lista))
