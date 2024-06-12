#szyfr CBC-MAC

def podziel(tekst,n):
    wynik = [tekst[i:i+n] for i in range(0,len(tekst),n)]
    for i in range(n-len(wynik[-1])):
        wynik[-1] = wynik[-1] + '0'
    return wynik

def xor(a,b):
    X=''
    for i,j in zip(a,b):
        x = str(int(i)^int(j))
        X += x
    return X

def blok(X,Pi):
    Z=''
    for i in range(len(X)):
        Z += X[Pi[i]]
    return Z 

def szyfr_CBC(P):
    y='0000'
    for X in P:
        wynik = xor(X,y)
        c = blok(wynik,Pi)
        y = c 
    return y

print('- Kod CBC-MAC -')
p=int(input("Podaj p: "))
print("hash : {0,1}* --> {0,1}^%d" %p)
tekst=input("Podaj tekst: ")
P=podziel(tekst,p)
Pi=eval(input("Podaj perm: "))
sz = szyfr_CBC(P)
print("(CBC-MAC)('%s') = %s" %(tekst,sz))