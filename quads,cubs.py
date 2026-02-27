def quads(numero):
    risultato=numero*numero
    return risultato


def cubs(numero):
    risultato=numero*numero*numero
    return risultato

n=5
c=quads(n)
q=cubs(n)
print(str(c)+" e "+ str(q))