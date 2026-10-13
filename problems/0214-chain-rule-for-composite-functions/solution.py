import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	def func(function:str,x:float):
		if function == 'square':
			func = pow(x,2)
		elif function == 'sin':
			func =np.sin(x)
		elif function == 'exp':
			func = np.exp(x)
		elif function == 'log':
			func = np.log(x)
		return func
	
	def der(function:str,x:float):
		if function == 'square':
			der = 2*x
		elif function == 'sin':
			der = np.cos(x)
		elif function == 'exp':
			der = np.exp(x)
		elif function == 'log':
			der = 1/x
		return der

    func_value = x
	gradient = 1.0
	for name in reversed(functions):
		gradient *=der(name,func_value)
		func_value = func(name,func_value)  
	return float(gradient)
