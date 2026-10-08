def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    der = c * n * pow(x,n-1)
    return float(der)