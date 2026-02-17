import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n=np.zeros((len(v),len(v)))
    for i in range(len(v)):
        n[i][i]=v[i]
    return n
                
