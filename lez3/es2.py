def palindromo(stringa):
    for i in range(len(stringa)//2):
        if stringa[i]==stringa[-i-1]:
            return True
        else: 
            return False
        


stringa="ciic"
print(palindromo(stringa))

