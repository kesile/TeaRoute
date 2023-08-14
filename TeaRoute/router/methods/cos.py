import math, numpy as np
from numpy.linalg import norm

def cos(vector1, vector2):

    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    cosine = np.dot(vector1,vector2)/(norm(vector1)*norm(vector2))  
    
    return cosine