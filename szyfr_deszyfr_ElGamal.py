def klucz(p,g,a):
    A = pow(g,a,p);
    return A

def szyfrowanie(g, p, A, b, x):
  B = pow(g, b, p)
  C = (x * pow(A, b, p)) % p
  return B, C

def deszyfrowanie(B, C, a, p):
  m = (C * pow(B, p-1-a, p)) % p
  return m






