#Protokół Diffiego-Hellmana

print("\t* PROTOKÓŁ DIFFIEGO-HELLMANA *")
p = int(input("Podaj p: "))
g = int(input("Podaj g: "))
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

A = pow(g,a,p)
B = pow(g,b,p)

K1 = pow(B,a,p)
K2 = pow(A,b,p)

print("A=%d^%d mod %d = %d" %(g,a,p,A))
print("B=%d^%d mod %d = %d" %(g,b,p,B))

print("\t- Wspólny klucz -")
print("K=%d^%d mod %d = %d" %(A,b,p,K1))
print("K=%d^%d mod %d = %d" %(B,a,p,K2))