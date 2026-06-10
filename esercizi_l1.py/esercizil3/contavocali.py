def conta(testo):
    vocali=("aeiou")
    conta=0
    for char in  testo:
        for carattere in vocali:
            if( char==carattere):
                conta=conta+1
    return conta
        

print(conta("Ciao mondo"))