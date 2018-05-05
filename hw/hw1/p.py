import pickle
with open('inv_list.pickle','rb') as f:
    inv_list = pickle.load(f)
print type(inv_list)
