import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	if func_name == 'poly2d':
		x,y = point 
		fx = 2*x*y + pow(y,2)
		fy = pow(x,2)+2*x*y 
		return (fx,fy)
	elif func_name == 'exp_sum':
			x,y = point
			v = np.exp(x+y)
			return(v,v)
	elif func_name == 'product_sin':
			x,y = point
			fx = np.sin(y)
			fy = x*np.cos(y)
			return(fx,fy)
	elif func_name == 'poly3d':
			x,y,z = point
			fx = 2*x*y
			fy = pow(x,2)+pow(z,2)
			fz = 2*y*z
			return(fx,fy,fz)
	else:
			x,y = point
			fx = 2*(x-y)
			fy = 2*(y-x)
			return(fx,fy)
