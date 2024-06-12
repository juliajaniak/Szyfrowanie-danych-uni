def nwd(a,b):
    if (b==0):
        return a
    return nwd(b,a%b)

def pub_wykl(p,q):
    e=3
    while((nwd(e,(p-1)*(q-1))!=1)or(e>=p*q)):
        e=e+2
    return e

def pryw_wykl(b,p,q):
    return pow(b,-1,(p-1)*(q-1))

def rsa_sig(x,a,n):
    return pow(x,a,n)

def rsa_ver(x,y,b,n):
    if pow(y,b,n)==x:
        print('\n\t\tver(%d,%d) = tak\n\n\t\tPodpis jest autentyczny!'%(y,x))
    else:
        print('\n\t\tPodpis jest podrobiony!')




