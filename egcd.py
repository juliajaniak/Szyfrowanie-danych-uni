def egcd(a,b):
    if a==0:
        return b,0,1
    else:
        d,y,x=egcd(b%a,a)
    return d,x-(b//a)*y,y

a=int(input('Podaj a: '))
b=int(input('Podaj b: '))

print('NWD(%d,%d)=%d=(%d)*%d+(%d)*%d' %(a,b,egcd(a,b)[0],egcd(a,b)[1],a,egcd(a,b)[2],b))

m=26

def inv(a,m):
    d,x,y=egcd(a,m)
    if d!=1:
        print('Błąd!')
    else:
        return x%m
    
print('%d^{-1} mod %d=%d' %(a,m,inv(a,m)))
