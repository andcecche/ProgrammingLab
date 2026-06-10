def forse(a,l):
    for i in a:
        for j in l:
            if(i==j):
                return True 
    return False
            

a=[1,1,1,1,1,1,1]
b=[2,2,2,2]

print(forse(a,b))