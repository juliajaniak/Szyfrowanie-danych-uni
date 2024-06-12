#Rekurencyjna funkcja skrótu

def str_to_list(x):
    lista = []
    n = len(x)
    
    for i in range(0,n):
        lista.append((ord(x[i])-96))
    return lista

def hash1(x,p):
    lista = str_to_list(x)
    h = 0
    
    for i in lista:
        h = (h+i)%p
    return h

print("\t-Rekurencja-")
x=input("Podaj x: ")
p=int(input("Podaj p: "))
print("hash('%s')=" %x,hash1(x,p))