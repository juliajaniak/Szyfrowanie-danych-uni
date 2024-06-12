def nwd(a,b):
    if (b==0):
        return a
    return nwd(b,a%b)

def pub_wykl(p,q):
    b=3
    while((nwd(b,(p-1)*(q-1))!=1)or(b>=p*q)):
        b=b+2
    return b
