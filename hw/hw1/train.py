import pickle
import spams
import numpy as np
with open('./hw1_data/LFW_DATA.pickle','rb') as f:
    data = pickle.load(f)
#print data.keys()
#[u'database_name', u'query_identity', u'database_identity', u'query_name', u'database_feature', u'query_feature']
src = data['database_feature']


# read attributes
with open('./hw1_data/lfw_attributes.txt') as f:
    ls = f.readlines()
"""
default target attribute : White
Inputs: 
    src, data from hw1_data.pickle which contain LBP for every imgae in LFW.
"""

def train_SC(src, K=400, lambda1=0.01, iter_=-10,out_file='./dict.npy'):

    num = src.shape[0]
    X = src.reshape([num, 80,59])
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
    with open(out_file,'wb') as f:
        np.save(f,D_list)
    print('Done')
    with open(out_file,'rb') as f:
        data = np.load(f)
    print(data.shape)

if __name__ == '__main__':
    train_SC(src, K=800)
