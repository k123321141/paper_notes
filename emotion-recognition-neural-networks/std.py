

from __future__ import division, absolute_import
import re
import numpy as np
from dataset_loader import DatasetLoader
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected, flatten
from tflearn.layers.conv import conv_2d, max_pool_2d, avg_pool_2d
from tflearn.layers.merge_ops import merge
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from constants import *
from os.path import isfile, join
import random
import sys

import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *

def res_cnn():
    face_input = Input(shape=[SIZE_FACE, SIZE_FACE, 1], name='face_input')
    x = face_input
    for i in range(4):
        short_cut = x
        f = 64 * (2**i)
#             block 1
        x = Conv2D(f , kernel_size=3, strides=2, data_format="channels_last", padding='same')(x)
        x = BatchNormalization(axis=-1)(x)
        x = Activation('relu')(x)
#             block 2, no activation function
        x = Conv2D(f , kernel_size=3, strides=1, data_format="channels_last", padding='same')(x)
        x = BatchNormalization(axis=-1)(x)
#             short_cut
        short_cut = Conv2D(f , kernel_size=3, strides=2, data_format="channels_last", padding='same')(short_cut)
        short_cut = BatchNormalization(axis=-1)(short_cut)
#             add
        x = add([x, short_cut])
        x = Activation('relu')(x)
#           
    x = Flatten()(x)
    x = AlphaDropout(0.3)(x)
    x = Dense(1024, activation='relu')(x)
    emo_class = Dense(len(EMOTIONS), activation='softmax')(x)

    model = Model(inputs=face_input, outputs=emo_class)
    
    return model

def std_cnn():
    face_input = Input(shape=[SIZE_FACE, SIZE_FACE, 1], name='face_input')
    x = face_input
    for i in range(3):
        x = Conv2D(64 * (2**i) , kernel_size=5, strides=2, data_format="channels_last", activation='linear', padding='same')(x)
        x = BatchNormalization(axis=-1)(x)
        x = Activation('relu')(x)
    x = Flatten()(x)
    x = AlphaDropout(0.3)(x)
    x = Dense(1024, activation='relu')(x)
    emo_class = Dense(len(EMOTIONS), activation='softmax')(x)

    model = Model(inputs=face_input, outputs=emo_class)
    return model

class EmotionRecognition:

    def __init__(self):
        self.dataset = DatasetLoader()

    def build_network(self):
        # Smaller 'AlexNet'
        # https://github.com/tflearn/tflearn/blob/master/examples/images/alexnet.py
        print('[+] Building CNN')
        
        self.model = res_cnn()
        
        self.model = std_cnn()
        
        opt = Adam(lr=0.001)
        self.model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
        
        self.model.summary()
#         self.load_model()
    
    def load_saved_dataset(self):
        self.dataset.load_from_save()
        print('[+] Dataset found and loaded')

    def start_training(self):
        self.load_saved_dataset()
        self.build_network()
        if self.dataset is None:
            self.load_saved_dataset()
        # Training
        print('[+] Training network')
        cks = keras.callbacks.ModelCheckpoint('./data/std', monitor='val_loss', save_best_only=True )
        logs = keras.callbacks.TensorBoard(log_dir='./std/logs')
        self.model.fit(
            self.dataset.images, self.dataset.labels,
            validation_split = 0.01,
#             validation_data=(self.dataset.images_test,
#                             self.dataset.labels_test),
            callbacks=[cks, logs],
            epochs=100,
            verbose=2,
            batch_size=256
        )

    def predict(self, image):
        if image is None:
            return None
        image = image.reshape([-1, SIZE_FACE, SIZE_FACE, 1])
        return self.model.predict(image)

    def save_model(self):
        self.model.save(join(SAVE_DIRECTORY, SAVE_MODEL_FILENAME))
        print('[+] Model trained and saved at ' + SAVE_MODEL_FILENAME)

    def load_model(self):
        SAVE_MODEL_FILENAME = 'emotion_recognition-21150.data-00000-of-00001'
        if isfile(join(SAVE_DIRECTORY, SAVE_MODEL_FILENAME)):
            #self.model.load(join(SAVE_DIRECTORY, SAVE_MODEL_FILENAME))
            self.model.load(join(SAVE_DIRECTORY,'emotion_recognition-21150'))
            print('[+] Model loaded from ' + SAVE_MODEL_FILENAME)
        else:
            print('[+]nont', join(SAVE_DIRECTORY, SAVE_MODEL_FILENAME))

def show_usage():
    # I din't want to have more dependecies
    print('[!] Usage: python emotion_recognition.py')
    print('\t emotion_recognition.py train \t Trains and saves model with saved dataset')
    print('\t emotion_recognition.py poc \t Launch the proof of concept')

mode = 'train'
if __name__ == "__main__":
#     if len(sys.argv) <= 1:
#         show_usage()
#         exit()
    network = EmotionRecognition()
    if mode == 'train':
        network.start_training()
        network.save_model()
    elif mode == 'poc':
        import poc
    else:
        show_usage()




