def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	n = len(matrix)

	trace = 0.0
	for i in range(n):
		trace += matrix[i][i]
	
	def det(matrix:list[list[float]]):
		n = len(matrix)
		
		if n == 1:
			return matrix[0][0]
		else:
			ans = 0.0
			for j in range(n):
				minor = [  row[:j]+row[j+1:] for row in matrix[1:]]
				ans += pow(-1,j)*matrix[0][j]*det(minor)
			return ans
	
	return(det(matrix),trace)