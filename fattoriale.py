def fact(num):
    prod=1
    while num!=1:
        prod=prod*num
        num=num-1
    return prod


print('inserire numero ')
n=int(input())
prod= fact(n)

print('Prodotto: '+str(prod))