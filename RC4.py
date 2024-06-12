#szyfr RC4 - szyfr strumieniowy (wszystko jest w dziedzinie do 8)

def wektor_stanu(T):
    S=[i for i in range(8)]
    j = 0
    for i in range(8):
        j = (j+S[i]+T[i])%8
        S[i],S[j]=S[j],S[i] #jest to taka nasza zamiana wartości w środku czyli takie permutacje
        #tylko tutaj jakby robimy to że dodajemy to co wychodzi, to co jest w S i to co podaliśmy 
        # w wektorze klucza
    return S
        
def generator_klucza(S):
    j=0
    K=[]
    for i in range(4):
        i = (i+1)%8
        j=(j+S[i])%8
        S[i],S[j]=S[j],S[i]
        t = (S[i]+S[j])%8
        K.append(S[t]) #w kluczu beda te elementy ktore juz sa w S ale moga sie powtarzać !
    return K
    
T=list(input("Podaj wektor klucza: ")) #podajemy wektor klucza o długości 8
for j in range(len(T)):
    T[j]=int(T[j])

S=wektor_stanu(T)
K=generator_klucza(S)
P=list(input("Podaj wektor tekstu: ")) #podajemy wektor tekstu o długości 4 czyli połowa
for j in range(len(P)):
    P[j]=int(P[j])

#bierzemy wektor tekstu podany oraz generator_klucza (z 8 mamy 4 elementy) ktory zostal stworzony z wektora stanu (permutacja) z wektora klucza
def RC4(P,K):
    lista = []
    for i in range(len(P)):
        liczba = int(P[i]) ^ int(K[i]) #xorujemy każdy element z każdym i mamy nasz szyfrogram
        lista.append(liczba)
    return lista

Sz=RC4(P,K)
print("Szyfrogram: ",Sz)