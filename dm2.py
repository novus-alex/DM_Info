"""
DM 2

Hachet Alexandre 833
"""

# Q1
def binaire(p, n):
	bin_ = [0]*n
	for i in range(n):
		bin_[i] = p%2
		p //= 2
	return bin_

#Q2
def somme_ss_ensemble(L, c):
	for p in range(2**len(L)):
		s, l, bin_ = 0, [], binaire(p, len(L))
		for i in range(len(bin_)):
			if bin_[i] == 1:
				l.append(i)
				s += L[i]
		if s == c:
			return True, l
	return False, []

#Q3
"""
La fonction somme_ss_ensemble est de complexité O(n*2**n)
"""

#Q4
"""
Si Xi-1 > j, alors il n'est pas possible d'exprimer Bi,j car X0,...,Xi-1 > j donc on doit forcément prendre au maximum Xi-2, ce qui correspond à Bi-1,j.
Sinon, on prend l'entier Xi-1 donc Bi,j = Bi-1,j-X(i-1) car on enlève le dernier entier pris ou Bi-1,j si on décide de ne pas prendre l'entier Xi
"""

#Q5
def mat_bool(L, c):
	m = [[False]*(c+1) for _ in range(len(L) + 1)]
	for i in range(len(L)+1):
		m[i][0] = True
	for i in range(len(L)+1):
		for j in range(1, c+1):
			if i == 0:
				m[0][j] = False
			elif L[i-1] > j:
				m[i][j] = m[i-1][j]
			else:
				m[i][j] = m[i-1][j-L[i-1]] or m[i-1][j]
	return m

#Q6
"""
Soit M la matrice calculer avec L et c, on prend i=n et j=c, tant que i est strictement positif, on regarde si M[i][j] est égale a M[i-1][j], si c'est le cas,
alors on enlève 1 à i, sinon on ajoute 1 a une liste A de taille n à l'indice i-1 et on remplace j par j - L[i-1].
On aura alors une liste nous donnant la positions des entiers dont la somme fais c.
Il reste plus qu'à reprendre ces indices dans la liste L et on auras la liste des éléments dont la somme fais c.
"""

#Q7
def somme_ss_ensemble2(L, c):
	A, r, i, j = [0]*len(L), [], len(L), c
	M = mat_bool(L, c)
	if M[len(L)][c]:
		while i > 0:
			if M[i][j] == M[i-1][j]:
				i -= 1
			else:
				A[i-1] += 1
				j -= L[i-1]
		for p in range(len(A)):
			if A[p]:
				r.append(L[p])
		return r
	else:
		return -1

#Q8
"""
On remarque que sans l'appel de mat_bool, notre fonction est de complexité O(n + c) car a chaque étape de la boucle while,
la quantité i + j décroît strictement. Or la focntion mat_bool a une complexité O(n*c), c'est donc cette fonction qui
donne la complexité O(n*s) à notre fonction somme_ss_ensemble2.
"""

#Q9
"""
On se rend compte que la première fonction somme_ss_ensemble est beacoup plus couteuse que la deuxième.
En effet en prennant n = len(L), sa complexité étant de O(n*2**n), elle est beaucoup plus grande que O(n*c).
On peut donc envisager que la première méthode sera plus efficace que la deuxième si la taille de L n'est pas trop grande,
sinon, il sera préférable de choisir la deuxième méthode.
"""

#Q10
def somme_rec(L, c):
	if c == 0:
		return True
	elif L == []:
		return False
	elif somme_rec(L[:-1], c):
		return True
	elif c >= L[-1]:
		return somme_rec(L[:-1], c-L[-1])
	else:
		return somme_rec(L[:-1], c)
