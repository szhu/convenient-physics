from math import factorial

def nCr(n,r):
	return factorial(n) / factorial(r) / factorial(n-r)

def nPr(n,r):
    return factorial(n) / factorial(n-r)