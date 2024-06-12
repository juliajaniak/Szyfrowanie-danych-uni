#Funkcja skrótu CHP
def HASH(x,y,a,b,p):
    return (pow(a,x,p)*pow(b,y,p))%p

#print("\t-Funkcja skrotu CHP-")
#p=int(input("Podaj p: "))
#q=int(input("Podaj q: "))

#a = int(input('Podaj a z ZZ(%d): '%p))
#b = int(input('Podaj b z ZZ(%d): '%p))

#print('Podaj tekst')
#x = int(input('Podaj x z ZZ(%d) : '%q))
#y = int(input('Podaj y z ZZ(%d) : '%q))
#print("hash(%d,%d)="%(x,y), HASH(x,y,a,b,p))