import numpy as np

def calculate_correlation_matrix(X, Y=None):
	x = np.asarray(X,dtype=float)
	if Y is None:
		y = x 
	else:
		y = np.asarray(Y,dtype=float)

	n = x.shape[1]
	p = y.shape[1]

	mean_x = x.mean(axis = 0)
	mean_y = y.mean(axis = 0)

	x_centered = x - mean_x
	y_centered = y - mean_y

	norm_x = np.linalg.norm(x_centered,axis = 0)
	norm_y = np.linalg.norm(y_centered,axis = 0)

	pro = x_centered.T@y_centered

	for i in range(n):
		for j in range(p):
			pro[i][j] /= norm_x[i]*norm_y[j]
	
	return pro


