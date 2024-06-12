#szyfr LFSR - liniowe sprzężenie zwrotne

def xor(a,b):
    X=''
    for i,j in zip(a,b):
        x = str(int(i)^int(j))
        X += x
    return X
#pokolei xorujemy dane wartości


def LFSR(n,seed):
    #zakładamy że m=4
    b1=seed[0]
    b2=seed[1]
    b3=seed[2]
    b4=seed[3]
    
    c=seed
    for i in range(4,n):
        t = xor(b1,b2)
        c += t
        b1 = b2
        b2 = b3
        b3 = b4
        b4 = t
    return c


seed=input("Podaj ziarno: ")
n=int(input("Podaj n: "))
wynik=LFSR(n,seed)
print("Strumień klucza: ",wynik)
