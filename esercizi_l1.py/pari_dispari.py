def pari_dispari(i):
    if (i%2==0):
        print(f"Il numero {i} è pari")
    else:
        print(f"il numero {i} è dispari")

print("inserisci un numero")
i=input()
pari_dispari(i)