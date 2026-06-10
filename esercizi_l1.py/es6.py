def conta(list):
    counter={}
    for parola in list:
        if parola in counter:
            counter[parola]+=1
        else:
            counter[parola]=1
    return counter

lista=["ciao","mciao","ciao","rama", "bataclan","hallal","skibidi toilet","loreal capelli","ciao"]
print(conta(lista))
