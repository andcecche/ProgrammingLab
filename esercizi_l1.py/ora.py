def ore_minuti(i):
    ore=0 
    while i>60 :
        ore=ore+1
        i=i-60
    print(f"Sono: {ore} ore e {i} minuti ")


i=538
ore_minuti(i)
