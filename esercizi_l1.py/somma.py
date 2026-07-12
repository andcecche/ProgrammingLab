def somma(i):
    somma=0
    while i!=0 :
        somma=somma+i
        i=input("Inserire nuovo numero")
    if (i==0):
        print(f"somma finita, il risultato :{somma} ")

i=input("inserire il primo numero, 0 per terminare")
somma(i)