import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    x = np.asarray(x,dtype = float)
    n = len(x)
    approximation_grad = np.zeros(n)
    for i in range(n):
        x1 = x.copy()
        x2 = x.copy()
        x1[i] += epsilon
        x2[i] -= epsilon
        approximation_grad[i] = ((f(x1)-f(x2))/(2*epsilon))

    delta = approximation_grad - analytical_grad
    norm_delta = np.linalg.norm(delta)
    norm_appr_grad = np.linalg.norm(approximation_grad)
    norm_anal_grad = np.linalg.norm(analytical_grad)
    if norm_appr_grad == norm_anal_grad == 0:
        relative_error = 0.0
    else:
        relative_error = norm_delta/(norm_anal_grad + norm_appr_grad)
    return approximation_grad, relative_error