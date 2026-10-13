import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	n = len(x)
	fx = f(x)
	m =len(fx)

	ans =[[0.0 for _ in range(n)] for _ in range(m)]

	for i in range(m):
		for j in range(n):
			x1 = x.copy()
			x1[j] += h
			f_new =f(x1)
			ans[i][j] = (f_new[i] - fx[i])/h
	return ans
			