import numpy as np
def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	z = max(logits)
	total = 0.0
	q = []
	for i in range(len(logits)):
		total += np.exp(logits[i]-z)
	q = [np.exp(x-z)/total for x in logits]
	
	y = [0.0 for _ in range(len(logits))]
	y[target] = 1
	return [q[x]-y[x] for x in range(len(q))]
