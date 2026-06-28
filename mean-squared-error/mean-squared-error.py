import numpy as np

def mean_squared_error(y_pred, y_true):
    n=len(y_true)
    sum=0;
    for i in range(n):
        sum+=(y_pred[i]-y_true[i])**2
    return (1/n)*(sum)

    
    
    
