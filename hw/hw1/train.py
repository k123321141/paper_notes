# train for attributed
import pickle
import numpy as np
import sparse_coding

lfw_path = './hw1_data/LFW_DATA.pickle'
with open(lfw_path, 'rb') as f:
    lfw = pickle.load(f)
database = lfw['database_feature']

param = { 'K' : 200,
              'lambda1' : 0.01, 'numThreads' : -1, 'mode':2,
              'iter' : -10}


D_list = sparse_coding.train_SC(database, param)
sparse_coding.save_D_list(D_list, out_file='./dict200.npy')
print('Done')