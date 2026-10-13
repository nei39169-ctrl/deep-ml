import numpy as np
def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	total =0.0
	n = len(x)
	ans =[[0.0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		total += np.exp(x[i])
	softmax = [np.exp(y)/total for y in x]
	
	def delta(i:int,j:int):
		if i == j:
			return 1
		else:
			return 0
	
	for i in range(n):
		for j in range(n):
			ans[i][j] = np.round(softmax[i]*(delta(i,j)-softmax[j]),4)
	
	return ans
