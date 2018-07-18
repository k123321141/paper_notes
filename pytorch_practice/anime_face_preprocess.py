# read anime-face csv
from os.path import join, isfile
import random
import pandas as pd
import os
import cv2
import numpy as np
from config import ANIME_PATH, ANNOTAION_PATH
from PIL import Image
from constants import imageSize, loadSize, channel_first
def read_img(path):
    im = Image.open(path).convert('RGB')
    im = im.resize( (loadSize, loadSize), Image.BILINEAR )
    arr = np.array(im)
    w1,w2 = (loadSize-imageSize)//2,(loadSize+imageSize)//2
    h1,h2 = w1,w2
    img = arr[h1:h2, w1:w2, :]
#     horizontal flip
    if random.randint(0,1):
        img=img[:,::-1]
    if channel_first:        
        img = np.moveaxis(img, 2, 0)
    return img
    

def naive_iterative_generator(shuffle=True):

    with open(ANNOTAION_PATH, 'r') as f:
        csv = pd.read_csv(f)
    #     
    img_paths = []
    tags = []
    for row in csv.iterrows():
        path, tag = row[1]
        img_paths.append(path)
        tags.append(tag)
        
#     generator, miss file count 28213, total count 143297.
    N = len(img_paths)
    while True:
        idxs = range(N)
        if shuffle:
            random.shuffle(idxs)
        for idx in idxs:
            path, tag = img_paths[idx], tags[idx]
            path = join(ANIME_PATH, path)
            if isfile(path):
                img = read_img(path)
                yield img, tag
    
def naive_bootsrap_generator():

    with open(ANNOTAION_PATH, 'r') as f:
        csv = pd.read_csv(f)
    #     
    img_paths = []
    tags = []
    for row in csv.iterrows():
        path, tag = row[1]
        img_paths.append(path)
        tags.append(tag)
        
#     generator, miss file count 28213, total count 143297.
    N = len(img_paths)
    while True:
        idx = random.randint(0,N)
        path, tag = img_paths[idx], tags[idx]
        path = join(ANIME_PATH, path)
        if isfile(path):
            img = read_img(path)
            yield img, tag


def img_generator(g):
    batch_size=1
    while True:
        imgs, tags = [],[]
        for i in range(batch_size):
            img, tag = g.next()
            h,w,dep = img.shape
            imgs.append(img.reshape([1, h, w, dep]))
            tags.append(tag)
        batch_size = ( yield np.vstack(imgs), tags )
        
#         
        if batch_size is None:
            batch_size = 1

    
def bootstrap_generator():
    g = naive_bootsrap_generator()
    img_g = img_generator(g)
    img, tag = img_g.next()
    return img_generator(g)

def iterative_generator(shuffle=True):
    g = naive_iterative_generator(shuffle)
    img_g = img_generator(g)
    img, tag = img_g.next()
    return img_g


