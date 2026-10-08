import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	ss = 0.0 
	for i in range(len(gradient)):
		ss += pow(gradient[i],2)
	magnitude = pow(ss,0.5)
	if magnitude == 0:
		direction =[0.0 for x in gradient]
		descent_direction =[0.0 for x in direction]
	else:
		direction = [x/magnitude for x in gradient]
		descent_direction = [x*(-1.0) for x in direction]
	return{'magnitude':magnitude,'direction':direction,'descent_direction':descent_direction}
