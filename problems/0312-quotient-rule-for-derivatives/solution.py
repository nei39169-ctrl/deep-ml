import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g_x, h_x = 0.0, 0.0
    der_g, der_h = 0.0, 0.0

    for i in range(len(g_coeffs)):
        g_x += g_coeffs[i] * pow(x, len(g_coeffs)-i-1)

    for i in range(len(h_coeffs)):
        h_x += h_coeffs[i] * pow(x, len(h_coeffs)-i-1)

    for i in range(len(g_coeffs)-1):
        exp = len(g_coeffs)-i-1
        der_g += g_coeffs[i] * exp * pow(x, exp-1)

    for i in range(len(h_coeffs)-1):
        exp = len(h_coeffs)-i-1
        der_h += h_coeffs[i] * exp * pow(x, exp-1)

    quo = (der_g * h_x - der_h * g_x) / pow(h_x, 2)

    return quo