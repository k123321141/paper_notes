import spams
import scipy

def load_D_list(in_file='./dict200.npy'):
    with open(in_file,'rb') as f:
        data = np.load(f)
    return data


def extract_name_idx_from_filename(s):
    s = s[0].split('\\')[-1].split('.jpg')[0]
    idx = int(s.split('_')[-1])
    buf = s.replace('_',' ').split(' ')[:-1]
    
    name = ''
    for b in buf:
        name += b
        name += ' '
    name = name.strip()
    return name, idx

def get_attribute_martix(features, identities, attribute_dict):
    X = np.zeros([ features.shape[0], 1])
    for i,f in enumerate(identities):
        name, idx = extract_name_idx_from_filename(f)
        value = 0
        if not attribute_dict.has_key(name):
            value = 0
        elif not attribute_dict[name].has_key(idx):
            value = 0
        else:
            value = attribute_dict[name][idx]
        X[i,0] = value
    return X

def get_weight_matrix(att, p=200, weight=float('inf'), var=120.):
#     W:  double p x n matrix   (weights)
    n = att.shape[0]
    W = np.ones([p,n])
    
#     ASC-D
#     for i,at in enumerate(att):
#         if at >= 0: # contain missing value
#             W[:p/2,i] = weight
#         else:
#             W[p/2:,i] = weight

#     ASC-W
    A = np.ones([p,])
    A[p/2:] = -1
    for i,at in enumerate(att):
        fa = np.repeat(at,p)
        assert fa.shape == (p, )
        W[:,i] = np.exp(np.abs(fa-A)/var)
    return np.asfortranarray(W)

def load_attribute_dict(path='./hw1_data/lfw_attributes.txt'):
    # prepare dict for attributes with name
    with open(path) as f:
        ls = f.readlines()
    at = ls[2:]
    attribute_dict = dict()
    for l in at:
        atts = l.strip().split('\t')
    #     print atts
        name,idx,male,asian,white = atts[0:5]
        if not attribute_dict.has_key(name):
            attribute_dict[name] = dict()
        attribute_dict[name][int(idx)] = float(white)
    return attribute_dict

def get_codeword(D_list, X, aX, lambda1=0.01, pathces_num=80):
    
    param = { 'lambda1' : lambda1, 'numThreads' : -1, 'mode':2}
    buf = []
    p = D_list.shape[-1]
    W = get_weight_matrix(aX,p)
    for i in range(pathces_num):
        q = np.asfortranarray(X[:,i,:])
        D = D_list[i]
        a = spams.lassoWeighted(q,D=np.asfortranarray(D),W=W,**param)
        buf.append(a)
    buf = scipy.sparse.vstack(buf)
    codeword = np.zeros(buf.shape, dtype=np.bool)
    codeword[buf.nonzero()] = True
    codeword = np.swapaxes(codeword, axis1=0, axis2=1)
    return codeword

database = lfw['database_feature']
file_names = lfw['database_identity'].ravel()
q_database = lfw['query_feature']
q_file_names = lfw['query_identity'].ravel()

attribute_dict = load_attribute_dict(path='./hw1_data/lfw_attributes.txt')

aX = get_attribute_martix(database, file_names, attribute_dict)
qaX = get_attribute_martix(q_database, q_file_names, attribute_dict)
print 'qax',qaX.shape
D_list = load_D_list('./dict200.npy')

p = D_list.shape[-1]
print p
query = lfw['query_feature']
query = query.reshape([-1,80,59])
query = np.swapaxes(query, 0, 2)
train_X = database.reshape([-1,80,59])
train_X = np.swapaxes(train_X, 0, 2)
print query.shape
db_sparse = get_codeword(D_list, train_X, aX)
print 'db done'
q_sparse = get_codeword(D_list, query, qaX)
W = get_weight_matrix(qaX)
# print q_sparse.shape
# print W[90:110,0],q_sparse[0,:]

print db_sparse.shape, q_sparse.shape
print 'shape done'