#szyfr ElGamal

def klucz(p,g,a):
    return pow(g,a,p)

def szyfrowanie (g,p,A,b,x):
    B = pow(g,b,p)
    C = (pow(A,b,p)*x)%p
    return B,C

def deszyfrowanie(B,C,a,p):
    c = p - 1 - a
    return (pow(B,c)*C)%p

p=int(input("Podaj p: "))
g=int(input("Podaj g: "))
a=int(input("Podaj a: "))

A=klucz(p,g,a)

print("Klucz publiczny: (%d,%d,%d)" %(p,g,A))
print("Klucz prywatny: ",a)

x=int(input("Podaj tekst: "))
b=int(input("Podaj b: "))

B,C = szyfrowanie(g,p,A,b,x)
print("Szyfrogram: (%d,%d)" %(B,C))
D=deszyfrowanie(B,C,a,p)
print("Wiadomość: ",D)