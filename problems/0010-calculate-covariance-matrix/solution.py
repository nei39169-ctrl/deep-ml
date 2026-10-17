import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	data = np.asarray(vectors,dtype = float)

	m,n = data.shape

	mean_data = np.mean(data,axis = 1,keepdims = True)
	centered_data = data - mean_data
	
	matrix = (centered_data@centered_data.T)/(n-1)

	return matrix.tolist()
 	
	
