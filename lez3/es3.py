def scambia(a,i,j):
    g=a[i]
    a[i]=a[j]
    a[j]=g
    for item in range(len(a)):
        print (a[item])


lista=["l","caz","ciao"]

scambia(lista,0,1)