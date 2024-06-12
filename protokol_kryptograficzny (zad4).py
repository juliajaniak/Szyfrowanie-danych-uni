import szyfr_deszyfr_ElGamal
import skrot_CHP
import podpis_weryfikacja_RSA

print("\t-SZYFR ELGAMAL-")
print("*Generowanie klucza*")
p = int(input("Podaj p: "))
g = int(input("Podaj g: "))
a = int(input("Podaj a: "))

A = szyfr_deszyfr_ElGamal.klucz(p,g,a)
print("Klucz publiczny: (%d,%d,%d)" %(p,g,A))
print("Klucz prywatny: ",a)

print("*Szyfrowanie*")
x=int(input("Podaj tekst: "))
b=int(input("Podaj b: "))

B,C = szyfr_deszyfr_ElGamal.szyfrowanie(g,p,A,b,x)
print("Szyfrogram: (%d,%d)" %(B,C))
x=szyfr_deszyfr_ElGamal.deszyfrowanie(B,C,a,p)

print("\t-SKROT CHP-")
p = int(input("Podaj p: "))
q=int(input("Podaj q: "))
a = int(input('Podaj a z ZZ(%d): '%q))
b = int(input('Podaj b z ZZ(%d): '%q))
z = skrot_CHP.HASH(B,C,a,b,p)
print("hash(%d,%d)="%(B,C),z)

print("\t- PODPIS RSA -")
print("*Generowanie klucza*")
p = int(input("Podaj p: "))
q = int(input("Podaj q: "))

n=p*q
b=podpis_weryfikacja_RSA.pub_wykl(p,q)
print("Klucz publiczny: (%d,%d)"%(n,b))

a=podpis_weryfikacja_RSA.pryw_wykl(b,p,q)
print("Klucz prywatny: ",a)

y=podpis_weryfikacja_RSA.rsa_sig(z,a,n)
print("Podpis: sig(%d)=" %z,y)

print("\t- SZYFROGRAM Z PODPISEM SKROTU -")
print("(B,C),y)=((%d,%d),%d)" %(B,C,y))

print("\t- WYZNACZENIE SKROTU -")
print("z = hash(%d,%d) = %d" %(B,C,z))
print("\t- WERYFIKACJA PODPISU -")
podpis_weryfikacja_RSA.rsa_ver(z,y,b,n)

print("- DESZYFROWANIE -")
print("Tekst odszyfrowany: ",x)