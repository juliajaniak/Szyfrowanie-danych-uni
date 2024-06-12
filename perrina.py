def perrina(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return perrina(n-2)+perrina(n-3)

n = int(input('Podaj n: '))
if perrina(n)%n != 0:
    print('Liczba %d jest na pewno złożona.'%n)
else:
    print('Liczba %d jest być może pierwsza.'%n)
