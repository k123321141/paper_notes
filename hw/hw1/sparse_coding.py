import pickle
import spams
import numpy as np
import scipy

pathces_num = 80
"""
default target attribute : White
Inputs: 
    src, data from hw1_data.pickle which contain LBP for every imgae in LFW.
"""

def train_SC(database, K=400, lambda1=0.01, iter_=-10,out_file='./dict.npy'):

    num = database.shape[0]
    X = database.reshape([num, 80,59])
    X = np.swapaxes(X,axis1=0,axis2=2)

    #lambda1 = [10**i for i in range(-6,-3,1)]
    #K = range(100,3200,400)
    param = { 'K' : K, # learns a dictionary with 100 elements
              'lambda1' : lambda1, 'numThreads' : -1, 'mode':2,
              'iter' : iter_}
        


    D_list = []
    pathces_num = X.shape[1]
    for i in range(pathces_num):
        x = np.asfortranarray(X[:,i,:])
        D = spams.trainDL(x,**param)
        D_list.append(D)
#     with open(out_file,'wb') as f:
#         np.save(f,D_list)
#     print('Done')
#     with open(out_file,'rb') as f:
#         data = np.load(f)
#     print(data.shape)
    return D_list

    
def get_codeword(D_list, X,lambda1=0.01):
    
    param = { 'lambda1' : lambda1, 'lambda2' : 0,'numThreads' : -1, 'mode':2}
    buf = []
    for i in range(pathces_num):
        q = np.asfortranarray(X[:,i,:])
        D = D_list[i]
        a = spams.lasso(q,D=D,return_reg_path = False,**param)
        buf.append(a)
    buf = scipy.sparse.vstack(buf)
    codeword = np.zeros(buf.shape, dtype=np.bool)
    codeword[buf.nonzero()] = True
    
    
    codeword = np.swapaxes(codeword, axis1=0, axis2=1)
    
    return codeword

def similarity_sparse_coding(codeword, query):
    q = query.ravel()
    
    distances = []
    for x in codeword:
#         distances.append(scipy.spatial.distance.hamming(x,query))
        distances.append(np.sum(np.logical_and(x,q)))
    return reversed(np.argsort(distances))


def sparse_coding(q_features, db_features):
    qs = q_features.reshape([len(q_features), 80,59])
    qs = np.swapaxes(qs,axis1=0,axis2=2)
    X = db_features.reshape([len(db_features), 80,59])
    X = np.swapaxes(X,axis1=0,axis2=2)
    
    D_list = train_SC(db_features, K=400, iter_=3)
    q_codeword = get_codeword(D_list, qs)
    db_codeword = get_codeword(D_list, X)
    return q_codeword, db_codeword

    
    
    
    
    
    
    
    