#Funkcja skrótu XOR

def podziel(bity):
    k=int(len(bity))//2
    L=[]
    L.append(bity[:k])
    L.append(bity[k:])
    return L

def tekst_do_bit(tekst):
    bit=''
    for j in tekst:
        j=str(bin(ord(j)))
        j=j.replace('0b','')
        bit+=j
    return bit

def xor(a,b):
    s=''
    for i,j in zip(a,b):
        k=int(i)^int(j)
        s+=str(k)
    return s

def HASH(tekst):
    bit=tekst_do_bit(tekst)
    L=podziel(bit)
    X=xor(L[0],L[1])
    return X


print("\t-Skrot XOR-")
x=input("Podaj x: ")
print("hash('%s')="%x, HASH(x))