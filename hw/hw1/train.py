import pickle
with open('./hw1_data/data.pickle','r') as f:
    data = pickle.load(f)
#print data.keys()
#[u'database_name', u'query_identity', u'database_identity', u'query_name', u'database_feature', u'query_feature']
src = data['database_feature']


# read attributes
with open('./hw1_data/lfw_attributes.txt') as f:
    ls = f.readlines()


import spams
import numpy as np
print src.shape
num = src.shape[0]
'''
# X = src.reshape([num, 80,59])

# X = np.swapaxes(X,axis1=0,axis2=2)
'''
X = src.reshape([num, 59,80])
X = np.swapaxes(X,axis1=0,axis2=1)
X = np.swapaxes(X,axis1=1,axis2=2)

lambda1 = [10**i for i in range(-6,-3,1)]
K = range(100,3200,400)
param = { 'K' : 1600, # learns a dictionary with 100 elements
          'lambda1' : 10**-3, 'numThreads' : 4, 'mode':2,
          'iter' : -800}
    
print X.shape


D_list = []
pathces_num = X.shape[1]
for i in range(pathces_num):
    print i
    x = np.asfortranarray(X[:,i,:])
    D = spams.trainDL(x,**param)
    D_list.append(D)
out_file = 'dict3.npy'
with open(out_file,'wb') as f:
    np.save(f,D_list)
print 'Done'
with open(out_file,'rb') as f:
    data = np.load(f)
print data.shape
