def NWD(a,b):
    if b>0:
        return NWD(b,a%b)
    return a
    
def pub_wykl(p,q):
    b = 3
    while ((NWD(b,(p-1)*(q-1))!=1) or (b>=p*q)):
        b += 2
    return b

def pryw_wykl(b,p,q):
    return pow(b,-1,(p-1)*(q-1))

p = int(input("Podaj p: "))
q = int(input("Podaj q: "))
x = int(input("Podaj tekst: "))

n=p*q
b=pub_wykl(p,q)

y=pow(x,b,n)
print("Szyfrogram: ",y)

a=pryw_wykl(b,p,q)
y1=pow(y,a,n)
print("Tekst odszyfrowany: ",y1)