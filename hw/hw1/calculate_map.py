import numpy as np
from l2_distance import *

def ap(idx_list, y):
    hit = 0
    n = 0
    precisions = []
    true_label_count = sum(y)
    for i in idx_list:
        y_true = y[i]
        n +=1
        if y_true == 1:
            hit += 1
            
            precisions.append(float(hit)/n)
            if hit == true_label_count:
                break
    ap = np.sum(precisions) / true_label_count
    return ap

def calculate_map(database, labels, queries, query_labels, similarity_func):
    APs = [] 
    i = 1
    for query,label in zip(queries,query_labels):
        idx_list = similarity_func(database, query)
        y = [1 if l == label else 0 for l in labels]
        APs.append(ap(idx_list, y))
#         print i
        i+=1
    mAP = np.mean(APs)
    return mAP
if __name__ == '__main__':
    import pickle
    with open('./hw1_data/LFW_DATA.pickle','rb') as f:
        data = pickle.load(f)
    src = data['database_feature']

    database = data['database_feature']
    labels = data['database_name'].ravel()

    queries = data['query_feature']
    query_labels = data['query_name'].ravel()
    mAP = calculate_map(database, labels, queries, query_labels, l2_distance)
    print(mAP)
    # print'mAP :  0.10249282626788106'