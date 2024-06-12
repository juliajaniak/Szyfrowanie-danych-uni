def nwd(a,b):
    if (b==0):
        return a
    return nwd(b,a%b)

def pub_wykl(p,q):
    e=3
    while((nwd(e,(p-1)*(q-1))!=1)or(e>=p*q)):
        e=e+2
    return e
    
p=int(input("\nPodaj p: "))
q=int(input("\nPodaj q: "))

n = p*q;
b = pub_wykl( p, q );
x = int(input("\nPodaj tekst x (0<x<%d):" %(n+1)))
y = pow( x, b, n )
print("\nSzyfrogram: %d" %y )
a = pow( b, -1,(p-1)*(q-1))
X = pow( y, a, n )
print("\nTekst odszyfrowany: %d" %X)

