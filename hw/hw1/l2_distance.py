# l2_distance.py
import numpy as np

# return index list with decreasing similarity
def l2_distance(database, query):
    q = query.ravel()
    
    #check feature dimension
    assert len(q) == 4720
    assert len(database.shape) == 2 and database.shape[1] == 4720
    distances = []
    for x in database:
        distances.append(np.linalg.norm(x-q,ord=2))
    return np.argsort(distances)