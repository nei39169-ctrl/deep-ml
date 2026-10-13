
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	total = 0.0 
	for i in range(len(L)):
		total += pow(L[i],2)
	modulus = pow(total,0.5)
	if len(v) == len(L):
		if modulus == 0:
			raise ValueError("L cannot be a zero vector")
		else:
			inner_product = 0.0
			for i in range(len(L)):
				inner_product += v[i]*L[i]
			return [inner_product/pow(modulus,2)*x for x in L]
	else:
		raise ValueError("Dimension mismatch")
	
			
