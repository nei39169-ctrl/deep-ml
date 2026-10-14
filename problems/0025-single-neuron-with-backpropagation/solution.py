import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	m,n = features.shape
	weights = initial_weights
	bias = initial_bias

	mse =[]
	for _ in range(epochs):
		"forward propagation"
		z = features@weights + bias
		h = 1/(1 + np.exp(-z))
		error =[h[x]-labels[x] for x in range(m)]

		"calculate mse for each epoch"
		error = h - labels
		loss = np.mean(error ** 2)
		mse.append(loss)

		"calculate parL/par wj "
		gradients = np.zeros(n)
		for j in range(n):
			total = 0.0
            for i in range(m):
                total += (
                    features[i][j]
                    * error[i]
                    * h[i]
                    * (1 - h[i])
                )
            gradients[j] = 2 * total / m

		"calculate parL/parb "
		total = 0.0
		for i in range(m):
			total += error[i]*(h[i])*(1-h[i])
		gradient_bias = total*2/m
		
		weights -= learning_rate * gradients
        bias -= learning_rate * gradient_bias
	
	return np.round(weights,4), np.round(bias,4), [np.round(x,4) for x in mse]