import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if arr.ndim == 1:
        if  norm_type  == 'l1':
            total = 0.0
            for i in range(len(arr)):
                total += abs(arr[i])
            return total
        elif norm_type == 'l2':
            total = 0.0
            for i in range(len(arr)):
                total += pow(arr[i],2)
            return pow(total,0.5)
        elif norm_type =='linf':
            norm = 0.0
            for i in range(len(arr)):
                if norm <= abs(arr[i]):
                    norm = abs(arr[i])
            return norm
        else :
           raise ValueError
    elif arr.ndim == 2:
        rows = arr.shape[0]
        columns = arr.shape[1]
        total = 0.0
        if norm_type =='l1':
            for i in range(rows):
                for j in range(columns):
                    total += abs(arr[i][j])
            return total
        elif norm_type =='l2'or norm_type =='frobenius':
            total = 0.0
            for i in range(rows):
                for j in range(columns):
                    total += pow(arr[i][j],2)
            return pow(total,0.5)
        elif norm_type =='linf':
            total = 0.0
            for i in range(rows):
                for j in range(columns):
                    if total <= abs(arr[i][j]):
                        total = abs(arr[i][j])
            return float(total)
        else:
            raise ValueError
    else:
        raise ValueError
        
                



                      
