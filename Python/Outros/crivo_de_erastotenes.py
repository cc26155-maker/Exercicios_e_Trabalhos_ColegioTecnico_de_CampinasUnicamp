import math as mt


def crivo(n):
    primos = [True for _ in range (n + 1)]
    primos[0] = primos[1] = False
    for i in range(2, int(mt.sqrt(n) + 1 )):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False
                
    return [x for x in range(n + 1) if primos[x]]


n = 100000
result = sum(crivo(n))
print(result)
