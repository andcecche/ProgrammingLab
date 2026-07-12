def fattoriale(i):
    while i>1:
        prodotto=i+fattoriale(i-1)
    return prodotto

i=input("Inserire numero per il calcolo del fattoriale:\n")
print=fattoriale(i)
