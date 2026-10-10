def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	m = len(vectors[0])
	n = len(vectors)
	residual =[]
	for i in range(n):
		tot_i = 0.0 
		for j in range(m):
			tot_i += vectors[i][j] 
		ave_i = tot_i/m
	    residual_i =[ x-ave_i for x in vectors[i]]
		residual.append(residual_i)
	cm =[]

	for i in range(n):
		row_i =[]
		for j in range(n):
			cov_ij = 0.0
			for k in range(m):
				cov_ij += residual[i][k]*residual[j][k]/(m-1)
			row_i.append(cov_ij)
		cm.append(row_i)
	return cm
	
	
	
