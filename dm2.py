"""
DM 2

Hachet Alexandre 833
"""

# Q1
def binaire(p, n):
	#assert 0 <= p and p <= 2**n - 1
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
Si Xi-1 > j, alors il n'est pas possible d'exprimer Bi,j car X0,...,Xi-1 > j donc on doit forcément prendre au maximu Xi-2, ce qui correspond à Bi-1,j.
Sinon, on prend l'entier Xi-1 donc Bi,j = Bi-1,j-X(i-1) car on enlève le dernier entier pris ou Bi-1,j si on décide de ne pas prendre l'entier Xi
"""

#Q5
def mat_bool(L, c):
	m = [[False]*(c+1)]*(len(L)+1)
	for i in range(len(L)+1):
		for j in range(c+1):
			if j == 0:
				m[i][j] = True
			elif i == 0 and j >= 1:
				m[i][j] = False
			elif L[i-1] > j:
				m[i][j] = m[i-1][j]
			else:
				m[i][j] = m[i-1][j-L[i-1]] or m[i-1][j]
	return m

#Q6
"""
On prend i=n et j=c, tant que i est strictement positif, on regarde si M[i][j] est égale a M[i-1][j], si c'est le cas,
alors on enlève 1 à i pour 
"""

#Q7
def somme_ss_ensemble2(L, c):
	A, i, j = [0]*len(L), len(L), c
	M = mat_bool(L, c)
	if M[i][j]:
		while i > 0:
			if M[i][j] == M[i-1][j]:
				i -= 1
			else:
				A[i] += 1
				j -= L[i]
		A[0] += j
		return A
	else:
		return -1

print(somme_ss_ensemble2([3, 1], 4))

