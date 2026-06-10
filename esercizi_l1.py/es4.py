def conta(parola, lettera):
    count=0
    for char in parola:
        if(char==lettera):
            count=count+1
    return count

p="banana"
l="a"
print(f"{conta(p,l)}")


