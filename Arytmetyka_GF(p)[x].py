from sympy.polys.domains import ZZ
from sympy.polys.galoistools import *

K = ZZ
p = 2

def bit_to_list(b):
    l=[]
    for i in b:
        l.append(int(i))
    return l

def list_to_bit(l):
    b=''
    for i in l:
        b+=str(i)
    return b

def add(f,g,p,K):
    print('\n\t',list_to_bit(gf_add(f,g,p,K)))

def mul(f,g,p,K):
    print('\n\t',list_to_bit(gf_mul(f,g,p,K)))

def rem(f,g,p,K): 
    print('\n\t',list_to_bit(gf_rem(f,g,p,K)))

def pot(f,n,g,p,K):
    print('\n\t',list_to_bit(gf_pow_mod(f,n,g,p,K)))

k=0
while k !=5:
    print('\n\tArytmetyka')
    print('\n\t1. Dodawania\n\t2. Mnożenie\n\t3. Reszta\n\t4. Potęgowanie\n\t5. Wyjście')
    k = int(input('\n\tPodaj wybor:\t'))
    if k==1:
        f1 = input('\n\tPodaj bity f:\t')
        f = bit_to_list(f1)
        g1 = input('\tPodaj bity g:\t')
        g = bit_to_list(g1)
        add(f,g,p,K)
    if k==2:
        f1 = input('\n\tPodaj bity f:\t')
        f = bit_to_list(f1)
        g1 = input('\tPodaj bity g:\t')
        g = bit_to_list(g1)
        mul(f,g,p,K)
    if k==3:
        f1 = input('\n\tPodaj bity f:\t')
        f = bit_to_list(f1)
        g1 = input('\tPodaj bity g:\t')
        g = bit_to_list(g1)
        rem(f,g,p,K)
    if k==4:
        f1 = input('\n\tPodaj bity f:\t')
        f = bit_to_list(f1)
        g1 = input('\tPodaj bity g:\t')
        g = bit_to_list(g1)
        n = int(input('\tPodaj n:\t'))
        pot(f,n,g,p,K)

    















