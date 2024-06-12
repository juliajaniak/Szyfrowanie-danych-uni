#Podpis ECDSA
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

def ecdsa_sig(g,p,q,A,a1,b1,t):
    A1,A2 = punkt_do_skladowych(A)
    u = (A1*b1)%q
    v = (A2*b1)%q
 
    B = u%q
    C = (((t+B*a1))*pow(b1,-1))%q
    return B,C

def ecdsa_ver(A,B,C,g,t,p,q):
    B,C = int(B), int(C)

    w = (pow(C,-1,q))%q
    i = (w*t)%q
    j = (w*B)%q

    x,y=punkt_do_skladowych(g)
    A1,A2 = punkt_do_skladowych(A)
    u1,u2 = mnozenie(x,y,i)
    v1,v2 = mnozenie(A1,A2,j)
    u,v,U= dodawanie(u1,u2,v1,v2)

    if u%q == B:
        print("ver(x,(%d,%d)) = tak" %(B,C))
        print("Podpis jest autentyczny!")
    else:
        print("ver(x,(%d,%d)) = nie" %(B,C))
        print("Podpis nie jest autentyczny!")

print("*Wybor krzywej*")
p=int(input('Podaj p: '))
a=int(input('Podaj a: '))
b=int(input('Podaj b: '))

print('E(%d;%d,%d)={(x,y): y^2=x^3+%dx+%d (mod %d)}\n'%(p,a,b,a,b,p))

print("*Generowanie klucza*")
p=int(input('Podaj p: '))
q=int(input('Podaj q: '))
g=input('Podaj g: ')
x,y=punkt_do_skladowych(g)
a1=int(input('Podaj a1: '))

A1,A2=mnozenie(x,y,a1)
print('Klucz publiczny: (g,A)=((%d,%d),(%d,%d))' %(x,y,A1,A2))
print('Klucz prywatny: a =',a1)

A=f"({A1},{A2})"

print("*Podpis skrótu*")
t=int(input("Podaj h(x): "))
b1=int(input("Podaj b: "))

B,C = ecdsa_sig(g,p,q,A,a1,b1,t)
print("sig(x,%d) = (%d, %d)" %(b1,B,C))

print("*Weryfikacja*")
ecdsa_ver(A,B,C,g,t,p,q)
