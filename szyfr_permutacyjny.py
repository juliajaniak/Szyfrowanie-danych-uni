import random

def szyfr_perm(X,Pi):
    Z = ''
    for i in range(len(X)):
        Z += X[Pi[i]]
    return Z

def perm(tekst):
    n = len(tekst)
    L = [i for i in range(0,n)]
    random.shuffle(L)
    return L
    

tekst = input("Podaj tekst: ")
#Pi = eval(input('Podaj perm: '))
Pi = perm(tekst)
print(Pi)
print(szyfr_perm(tekst,Pi))

