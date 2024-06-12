#szyfr ElGamal na krzywych eliptycznych
def Lambda(x1,y1,x2,y2,a,p):
    if x1==x2 and y1==y2:
        return ( (3*pow(x1,2,p)+a) * pow(2*y1,-1,p) )%p
    return ( (y2-y1) * pow(x2-x1,-1,p) )%p

def dodawanie(x1,y1,x2,y2):
    C=Lambda(x1,y1,x2,y2,a,p)
    x3=(C**2-x1-x2)%p
    y3=(C*(x1-x3)-y1)%p
    return x3,y3,C

def mnozenie(x,y,n):
    if n == 1:
        return x,y
    else:
        x1,y1,C = dodawanie(x,y,x,y)
        for i in range(n-2):
            x1,y1,C=dodawanie(x,y,x1,y1)
        return x1,y1
    
def przeciwny(x,y):
    return x, (-y)%p

def punkt_do_skladowych(P):
    P=P.split(',')
    L=[]
    for p in P:
        L.append(p)
    C1=int((L[0])[1:])
    C2=int((L[1])[:-1])
    return C1,C2

p=int(input('Podaj p: '))
a=int(input('Podaj a: '))
b=int(input('Podaj b: '))

print('E(%d;%d,%d)={(x,y) : y^2=x^3+%dx+%d (mod %d)}\n'%(p,a,b,a,b,p))

g=input('Podaj g: ')
x,y=punkt_do_skladowych(g)
print(x,y)
a1=int(input('Podaj a1: '))


A1,A2=mnozenie(x,y,a1)
print(x,y,a1,A1,A2)
print('Klucz publiczny: ')
print('(g,A)=((%d,%d),(%d,%d))' %(x,y,A1,A2))
print('Klucz prywatny:\n','a1 =',a1)
t=input('Podaj x: ')
x1,y1=punkt_do_skladowych(t)

b1=int(input('Podaj b1: '))
B1,B2=mnozenie(x,y,b1)
E1,E2=mnozenie(B1,B2,a1)
C1,C2,C=dodawanie(x1,y1,E1,E2)
print('Szyfrogram:')
print('((%d,%d),(%d,%d))' %(B1,B2,C1,C2))
e1,e2=przeciwny(E1,E2)
D1,D2,D=dodawanie(C1,C2,e1,e2)
print('Tekst:')
print('(%d,%d)' %(D1,D2))