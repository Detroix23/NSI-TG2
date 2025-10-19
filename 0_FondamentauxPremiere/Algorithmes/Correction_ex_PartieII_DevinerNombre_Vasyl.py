from random import randint

def DevinerNombre(N):
    s = 0
    check = False
    while check==False:
        a = int(input("Gues: "))
        if a < N:
            print("plus")
            s += 1
        if a > N:
            print("moins")
            s += 1
        if a == N:
            print("gj, nb of try", s)
            check = True      
    return s
    
G=int(input("Limit is: "))
DevinerNombre(randint(0,G))