"""
DM 3

Hachet Alexandre 833
"""

# Q1
def verifie_01(L):
    for i in L:
        if i != 0 and i != 1:
            return False
    return True

# Q2
def entier_naturel(L):
    s = 0
    for i in range(len(L)):
        s += L[i]*2**i
    return s

# Q3
def entier_relatif(L):
    return entier_naturel(L[:-1]) - L[-1]*2**(len(L)-1)

# Q4
def representation_naturel(x, n):
    assert x < 2**n, f"x >= {2**n}"

    b = []
    for i in range(n):
        b.append(x%2)
        x //= 2
    return b

# Q5
def representation_relatif(x, n):
    assert x >= -2**(n-1) or x < 2**(n-1)

    b = []
    if x > 0:
        b = representation_naturel(x, n-1)
        b.append(0)
    else:
        b = representation_naturel(x + 2**(n-1), n-1)
        b.append(1)
    return b

# Q7
def addition1(a, b):
    assert a in [0, 1] and b in [0, 1]

    if a+b == 2:
        return 0, 1
    else:
        return a+b, 0

# Q7
def addition2(a, b, c):
    add1 = addition1(a, b)
    if add1[0]+c == 2:
        return 0, 1
    return add1[0]+c, add1[1]

# Q8
def addition_listes(L, M, re):
    assert len(L) == len(M)

    T = []
    for i in range(len(L)):
        result = addition2(L[i], M[i], re)
        T.append(result[0])
        re = result[1]
    return T, T[-1], re

# Q9
def additionneur(L, M):
    result = addition_listes(L, M, 0)
    if result[2] == 1:
        print("Dépassement sur les entiers naturels")
        if result[1] != result[2]:
            print("Dépassement sur les entiers relatifs")
    elif result[1] != result[2]:
        print("Dépassement sur les entiers relatifs")
    return result[0]

# Q10
def complementaire(M):
    return [1 if _ == 0 else 0 for _ in M]

"""
Soit (An) tel que Nm = An-1....A0 et (Bn) tel que Nm(comp) = Bn-1.....B0 avec (An) et (Bn) à valeurs dans {0,1}
D'après la définition du complémentaire, pour tout k <= n-1, Ak != Bk donc comme (An) et (Bn) sont à valeurs dans {0,1},
On a Ak + Bk = 1, d'où Nm + Nm(comp) = (An-1+Bn-1)....(A0+B0) = 11....1 en base 2, ce qui est égale a -1 en décimal.
On a donc Nm + Nm(comp) = -1 ce qui équivaut à Nm(comp) + 1 = -Nm
"""

def soustracteur(L, M):
    result = addition_listes(L, complementaire(M), 1)
    if result[2] == result[0][0]:
        print("Dépassement sur les entiers relatifs")
    return result[0]