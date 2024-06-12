#protokół BB84
from Bases import *
import random
O = { I1: '0', I2: '1', I3: '0', I4: '1'}
plik_A = open('Alicja.txt','w')

def Bits(n):
    Bit = ''
    for i in range(n):
        j = random.randint(0,1)
        Bit += B[j]
    return Bit

def Bases(n):
    Bas = ''
    for i in range(n):
        j = random.randint(0,1)
        Bas += L[j]
    return Bas

def Bit_to_Qubit_A(Bit, Base):
    z = zip(Bit, Base)
    Q = []
    for i,j in z:
        if i == '0' and j=='+':
            Q.append(I1)
        if i =='0' and j=='×':
            Q.append(I3)
        if i == '1' and j == '+':
            Q.append(I2)
        if i == '1' and j == '×':
            Q.append(I4)
    return Q

def Bit_to_Qubit_B(Qubit, Base):
    z = zip(Qubit, Base)
    B = []
    
    #polaryzacja
    for i,j in z:
        if i == I1 and j=='+':
            B.append(I1)
        if i == I2 and j=='+':
            B.append(I2)
        if i == I3 and j == '+':
            B.append(I1 or I2)
        if i == I4 and j == '+':
            B.append(I1 or I2)
            
        if i == I1 and j=='×':
            B.append(I3 or I4)
        if i == I2 and j=='×':
            B.append(I3 or I4)
        if i == I3 and j == '×':
            B.append(I3)
        if i == I4 and j == '×':
            B.append(I4)
    return B

def veryfikacja(Base_A, Base_B):
    Ver = []
    AB = []
    for i in range(len(Base_A)):
        if Base_A[i] == Base_B[i]:
            Ver.append(V)
            AB.append(Qb_A[i])
        else:
            Ver.append('-')
            AB.append('-')
    return Ver, AB

def Qubit_to_Bit(T):
    B = []
    for i in T:
        if i in O:
            b = O[i]
            B.append(b)
    return B

print("* PROTOKOL BB84 *")
n = int(input("Podaj liczbe Qubitow: "))
Bit_A = Bits(n)
Base_A = Bases(n)

plik_A.write(Bit_A)
plik_A.write('\n')
plik_A.write(Base_A)
plik_A.close()

Qb_A = Bit_to_Qubit_A(Bit_A, Base_A)
print("Qubity Alicji")
print(Qb_A)

Base_B = Bases(n)
print("Baza Bolka")
print(Base_B)

Qb_B = Bit_to_Qubit_B(Qb_A, Base_B)
print("Qubity Bolka")
print(Qb_B)

print("Weryfikacja bazy Bolka")
Ver, AB = veryfikacja(Base_A, Base_B)
print(Ver)

print("Wspolne Qubity Alicji i Bolka")
print(AB)

print("Uzgodniony klucz Alicji i Bolka")
B = Qubit_to_Bit(AB)
Bity_AB = ''.join(B)
print(Bity_AB)

print("Liczba Bitow: ", len(B))