def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m = len(matrix)
	n = len(matrix[0])
	res=[]
	if mode =='column':
		for j in range(n):
			s =0.0
			for i in range(m):
				s +=matrix[i][j]
			mean_j = s/m
			res.append(mean_j)
		return res
	else:
		for i in range(m):
			s =0.0
			for j in range(n):
				s +=matrix[i][j]
			mean_i = s/n 
			res.append(mean_i)
		return res