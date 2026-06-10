my_dict={0:'zero',1:'uno',2:'due'}

def converti(l):
    add=[]
    for i in range(len(l)):
        add.append(my_dict[l[i]])
    print(add)

l=[0,1,2,2]
converti(l)