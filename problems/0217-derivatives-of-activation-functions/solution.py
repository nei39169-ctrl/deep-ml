import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	if x <=0:
		der_relu = 0 
	else:
		der_relu = 1
	
	sigmoid = 1/(1 + np.exp((-1)*x))
	der_sigmoid = sigmoid*(1-sigmoid)

	tanh = 1 - 2/(np.exp(2*x) + 1)
	der_tanh = 1 - pow(tanh,2)

	return{'sigmoid':der_sigmoid,'tanh':der_tanh,'relu':der_relu}