def NWD(a,b):
    if b>0:
        return NWD(b,a%b)
    return a
    
def pub_wykl(p,q):
    b = 3
    while ((NWD(b,(p-1)*(q-1))!=1) or (b>=p*q)):
        b += 2
    return b

p = int(input("Podaj liczbę p: "))
q = int(input("Podaj liczbę q: "))
n=p*q

b=pub_wykl(p,q)

x=input("Podaj tekst: ")


def pryw_wykl(b,p,q):
    return pow(b,-1,(p-1)*(q-1))

def str_to_nr(s):
    k = 0
    for i, j in enumerate(s):
        k += (ord(j) - 97) * (26 ** i)
    return k

def nr_to_str(n):
    s=''
    while n>0:
        n,i=divmod(n,26)
        s+=chr(i+97)
    return s

x1=str_to_nr(x)
y=pow(x1,b,n)
y2=nr_to_str(y)
print("Szyfrogram: ",y2)
a=pryw_wykl(b,p,q)
y1=pow(y,a,n)
y3=nr_to_str(y1)
print("Tekst odszyfrowany: ",y3)