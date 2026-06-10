def triangolo(l1,l2,l3):
    if(l1+l2>l3 and l1<l2+l3 and l1+l3>l2):
        print("è un triangolo")
        
        if(equil(l1,l2,l3)!=True):
            
            if(iso(l1,l2,l3)!=True):
                scal(l1,l2,l3)


def equil(l1,l2,l3):
    if(l1==l2 and l2==l3):
        print("è equilatero")
        return True
        

def iso(l1,l2,l3):
    if(l1==l2 or l2==l3 or l3==l1):
        print("è isoscele")
        return True

def scal(l1,l2,l3):
    print("è scaleno")

triangolo(3,3,3)