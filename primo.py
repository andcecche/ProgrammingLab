print('Numero:')
numero=int(input())
i=2
while i<numero:
    if numero%i==0:
        print('No primo')
        break
    i=i+1
if i==numero:
    print('primo')
