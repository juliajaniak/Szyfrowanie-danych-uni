def szyfr_afiniczny(a,b,tekst):
    szyfr =''
    
    for litera in tekst:
        d = chr((((ord(litera)-97)*a+b)%26)+97) ##na poczatku musimy od kodu ascii odjąć 97 i to jest nasz x
        # mamy wzór ax+b mod26
        #później żeby wrócić musimy dodać na nowo 97 i odczytać liczbę
        szyfr += d
    return szyfr
    
tekst=input("Podaj tekst: ")
a=int(input("Podaj a: "))
b=int(input("Podaj b: "))

if a==1:
    if b==3:
        print("Szyfr cezara")
    elif b==13:
        print("Szyfr ROT13")
else:
    print("Szyfr afiniczny")

szyfrogram = szyfr_afiniczny(a,b,tekst)
print("Szyfrogram: ",szyfrogram)

def egcd(a,b): #największy wspólny dzielnik NWD, ax+by=NWD(a,b)
    if a==0:
        return b,0,1 #jeżeli a jest równe 0 to b jest największym wspólnym dzielnikiem (b=0*a+b*1)
    else:
        d,x,y=egcd(b%a,a) #rekurencyjnie wyliczamy sobie d, x i y
    return d,y-(b//a)*x,x #x obliczamy jako odejmowanie od calosci b//a razy y tzw. q czyli o ile powiększamy

#a=int(input('Podaj a: '))
#b=int(input('Podaj b: '))

#print('NWD(%d,%d)=%d=(%d)*%d+(%d)*%d' %(a,b,egcd(a,b)[0],egcd(a,b)[1],a,egcd(a,b)[2],b))
#print(egcd(a,b))

def odwrotnosc_modulo(a,m=26):
    d,x,y=egcd(a,m)
    if d!=1:
        print('Błąd!')
    else:
        return x%m #to drugie czyli x musimy zrobić przez modulo 26 a*x=1mod26
#print(odwrotnosc_modulo(3))
    
#x=a^-1(y-b)mod26 gdzie a*a^-1=1mod26


def deszyfr_afiniczny(a,b,szyfrogram):
    tekst=''
    A = odwrotnosc_modulo(a) #na poczatku musimy miec odwrotnosc modulo od poczatkowego a
    for litera in szyfrogram:
        e = chr((A*((ord(litera)-97)-b))%26+97) #czyli to odwrocone a pomnozone przez wyliczenie ord(litera-97) od tego odejmujemy b i mod26 no i chcemy
        #odczytac te znaki no to od nowa chr
        tekst += e
    return tekst

print("Tekst odszyfr: ", deszyfr_afiniczny(a,b,szyfrogram))
    
