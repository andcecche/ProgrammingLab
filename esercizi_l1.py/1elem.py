def controllo(lista1,lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
            break

lista1=[1,2,2,2,2,2,3]
lista2=[8,9,9,9,3]
x=controllo(lista1,lista2)
print(x)