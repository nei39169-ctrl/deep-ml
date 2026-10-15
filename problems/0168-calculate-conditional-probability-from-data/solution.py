import numpy as np
def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    count_x = sum(x in sample for sample in data)
    count_xy = sum(x in sample and y in sample for sample in data)

    if count_x == 0:
      return 0.0
    else:
      return np.round(count_xy/count_x,4)