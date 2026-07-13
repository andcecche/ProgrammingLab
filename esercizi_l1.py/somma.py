def somma(i):
    somma=0
    while i>0 :
        somma=somma+i
        i=int(input("Inserire nuovo numero: \n"))
    if (i==0):
        print(f"somma finita, il risultato : {somma} ")

i=int(input("inserire il primo numero, 0 per terminare"))
somma(i)