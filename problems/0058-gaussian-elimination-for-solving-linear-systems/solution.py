import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	n = len(b)
	A = np.array(A,dtype=float,copy=True)
	b = np.array(b,dtype=float,copy=True)
	x = np.zeros(n)
	for k in range(n):
		pivot = k + np.argmax(np.abs(A[k:,k]))
		A[[pivot,k]] = A[[k,pivot]]
		b[[pivot,k]] = b[[k,pivot]]

		for i in range(k+1,n):
			factor = A[i][k]/A[k][k]
			A[i,k:] -= factor*A[k,k:]
			b[i] -= factor*b[k]

	x[n-1] = b[n-1]/A[n-1,n-1]	
	for k in range(n-2,-1,-1):
		x[k] = (b[k] - np.dot(A[k,k+1:], x[k+1:]))/A[k][k]
		

	return x
