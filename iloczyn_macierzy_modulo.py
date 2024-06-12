import numpy as np
from numpy import dot

def iloczyn_macierzy(A,B,m):
    return dot(A, B) % m
