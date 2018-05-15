from l2_distance import l2_distance #l2_distance.py
from sparse_coding import sparse_coding,similarity_sparse_coding #sparse_coding.py
from calculate_map import calculate_map #calculate_map.py
import pickle
lfw_path = './hw1_data/LFW_DATA.pickle'
with open(lfw_path, 'rb') as f:
    lfw = pickle.load(f)
database = lfw['database_feature']
queries = lfw['query_feature']
labels = lfw['database_name'].ravel()
query_labels = lfw['query_name'].ravel()

#part 3
lambda1 = [10**i for i in range(-4,-1,1)]
K = range(40,1600,100)
K = [40 * 2**i for i in range(6)]
iter_ = 1
for k in K:
    for l1 in lambda1:
        

        param = { 'K' : k,
                  'lambda1' : l1, 'numThreads' : -1, 'mode':2,
                  'iter' : iter_}
        print('starting Train')
        
        q_sparse, db_sparse = sparse_coding(lfw['query_feature'], lfw['database_feature'], param) #build sparse dict and lookup using spams library
        print('starting mAP')
        
        sparse_map = calculate_map(db_sparse, labels, q_sparse, query_labels, similarity_sparse_coding)# results_sparse = distance(q_sparse, db_sparse) #you can use l2_distance in part1 or try any distance metric, like cos, l1 

        print('performance',k,l1, sparse_map)
        
#         123






