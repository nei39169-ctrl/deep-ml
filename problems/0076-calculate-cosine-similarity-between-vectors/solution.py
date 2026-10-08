import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	sum_v1 = sum_v2 = pro =0.0
	for i in range(len(v1)):
		sum_v1 +=pow(v1[i],2)
		sum_v2 +=pow(v2[i],2)
		pro +=v1[i]*v2[i]
	norm_v1 = pow(sum_v1,0.5)
	norm_v2 = pow(sum_v2,0.5)
	res = pro/(norm_v1*norm_v2)
	return res