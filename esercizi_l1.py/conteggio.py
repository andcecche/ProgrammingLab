my_dict = {}

def conta(lista):
    for elemento in lista: 
        if elemento in my_dict:
            my_dict[elemento]+=1
        else:
            my_dict[elemento]=1
    return my_dict


lista=["Anna","Gio","Anna","Alma"]
print(conta(lista))