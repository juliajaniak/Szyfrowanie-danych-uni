def zamien(B):
    D=[]
    n = len(B)
    for i in range(n):
        D.append(B[n-i-1])
    return D

def poly_to_list(f):
    f = f.split('+')
    d = {}
    L = []
    for k in f:
        L.append(int(k[2:]))
    for i in range(0,L[0]+1):
        if i in L:
            d[i] = 1
        else:
            d[i] = 0
    K = list(d.values())
    return zamien(K)

'''while True:
    f = input('Podaj f: ')
    print(poly_to_list(f))'''
