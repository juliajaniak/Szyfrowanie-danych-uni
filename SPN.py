#szyfr SPN

k= '00111010100101001101011000111111'
#reprezentuje bity klucza

k1=k[:16]
k2=k[4:20]
k3=k[8:24]
k4=k[12:28]
k5=k[16:]
#klucze rund


K=[k1,k2,k3]
pi_S=[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
pi_P= [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
#permutacje

Bin=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
#przejście na kod dwójkowy

def xor(a,b):
    x = int(a)^int(b)
    return x

def U(w,k):
    #ciągi bitów w i ciąg bitów kluczy
    u=''
    for i in range(len(w)):
        u+=str(xor(w[i],k[i]))
    return u

def V(u):
    # z poprzedniego bierzmy nasze u i dzielimy na co 4
    U=[int(u[0:4],2),int(u[4:8],2),int(u[8:12],2),int(u[12:16],2)]
    v=''
    for i in U:
        #bierzemy pokolei w tym U wszystkie liczby i tłumaczymy wynik na dwójkowy
        v+=Bin[pi_S[i]]
    return v
       
def W(v):
    w=''
    for i in range(len(pi_P)):
        #a tu tłumaczymy na pi_P
        w+=v[pi_P[i]]
    return w

def Y(v):
    y=''
    for i in range(len(v)):
        y+=str(xor(v[i],k5[i]))
        #z tą ostatnią przyrównujemy i z v
    return y

def SPN(tekst):
    w=tekst
    for klucz in K:
        u=U(w,klucz)
        #każdy klucz z naszym tekstem musi być przerobiony
        v=V(u)
        v='x'+v
        w=W(v)
    u=U(w,k4)
    #na sam koniec robimy jeszcze raz to u ale z przerobionym w i k4
    v=V(u)
    y=Y(v)
    return y[0:4]+y[4:8]+y[8:12]+y[12:16]
        
        
tekst=input("Podaj tekst: ")
print('Szyfrogram: ',SPN(tekst))
