def szybkie_pot(a,b,n):
    X=a
    E=b
    Y=1
    while E>0:
        if E%2==0:
            X=(X*X)%n
            E=E/2
        else:
            Y=(X*Y)%n
            E=E-1
    return Y

#print(szybkie_pot(1,7,15))
