# -*- coding: utf-8 -*-
import numpy as np
import cv2 
from time import time
from os.path import join
import random, os
from tqdm import tqdm


CASC_PATH = join('./','haarcascade_files','haarcascade_frontalface_default.xml')
cascade_classifier = cv2.CascadeClassifier(CASC_PATH)
    

def detect_face(image, return_max_area_face=True):
    if len(image.shape) > 2 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image = cv2.imdecode(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    faces = cascade_classifier.detectMultiScale(
        image,
        scaleFactor=1.3,
        minNeighbors=5
    )
    # None is we don't found an image
    if not len(faces) > 0:
        return []
    if return_max_area_face:
        max_area_face = faces[0]
        for face in faces:
            if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
                max_area_face = face
        faces = [max_area_face, ]

    return faces

def bounding_face(frame, faces, factor, constraint=None):
    bounding_box_list = []
    
    for face in faces:
        x,y,w,h = face
        factor = 2.
        offset = (factor-1)/2.
        rect = [x-offset*w, y-offset*h, w*factor, h*factor]
        for i,a in enumerate(rect):
            rect[i] = int(a)
        rect = tuple(rect)



        x,y = rect[:2]
        x2 = x + rect[2]
        y2 = y + rect[3]
        box = (int(x), int(y)), (int(x2), int(y2))
        
        if constraint:
            if constraint(box):
                bounding_box_list.append(box)
        else:
            bounding_box_list.append(box)
    return bounding_box_list
def bounding_face_fixed_size(frame, faces, fixed_size, constraint=None):
    bounding_box_list = []
    for face in faces:
        x,y,w,h = face
        offset_x = (fixed_size-w)/2.
        offset_y = (fixed_size-h)/2.
        rect = [x-offset_x, y-offset_y, fixed_size, fixed_size]
        for i,a in enumerate(rect):
            rect[i] = int(a)
        rect = tuple(rect)

        

        x,y = rect[:2]
        x2 = x + rect[2]
        y2 = y + rect[3]
        box = (int(x), int(y)), (int(x2), int(y2))
        if constraint:
            if constraint(box):
                bounding_box_list.append(box)
        else:
            bounding_box_list.append(box)
    return bounding_box_list
def draw_bounding_box(frame, bounding_box_list):
    for box in bounding_box_list:
        (x, y), (x2, y2) = box
        cv2.rectangle(frame, (x, y), (x2, y2) , color=(255,255,255), thickness=5)
    return frame
def crop_bounding_box(frame, bounding_box_list):
    frame_list = []
    for box in bounding_box_list:
        (x, y), (x2, y2) = box
        f = frame[y:y2,x:x2,:]
        frame_list.append(f)
    return frame_list

def demo(video_path, constraint=None, return_max_area_face=True, factor=None, fixed_size=None, skip_beg_frame=0):
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(video_path)
    for i in range(skip_beg_frame):
        ret, frame = cap.read()
    while(cap.isOpened()):

        ret, frame = cap.read()
        faces = detect_face(frame, return_max_area_face)
        if factor:
            bounding_box_list = bounding_face(frame, faces, factor, constraint)
        elif fixed_size:
            bounding_box_list = bounding_face_fixed_size(frame, faces, fixed_size, constraint)
        else:
            print 'error'
            break
        frame = draw_bounding_box(frame, bounding_box_list)
        cv2.imshow('frame',frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('k'):
            for i in range(random.randint(0,200)):
                ret, frame = cap.read()


    cap.release()
    cv2.destroyAllWindows()

def crop_video(video_path, ouptut_path, constraint=None, return_max_area_face=True, factor=None, fixed_size=None, skip_beg_frame=0):
    cap = cv2.VideoCapture(video_path)
    frame_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    with tqdm(total=frame_length) as pbar:



        for i in range(skip_beg_frame):
            ret, frame = cap.read()
            pbar.update(1)
        existed_jpgs = [f for f in os.listdir(ouptut_path) if f.endswith('.jpg')]
        idx = len(existed_jpgs)
        print 'start from idx : %d' % idx
        while(cap.isOpened()):

            ret, frame = cap.read()
            if not ret:
                break
            pbar.update(1)
            faces = detect_face(frame, return_max_area_face)
            if factor:
                bounding_box_list = bounding_face(frame, faces, factor, constraint)
            elif fixed_size:
                bounding_box_list = bounding_face_fixed_size(frame, faces, fixed_size, constraint)
            else:
                print 'error'
                break
            frame_list = crop_bounding_box(frame, bounding_box_list)
            for frame in frame_list:
                out_path = join(ouptut_path,'%d.jpg' % idx)
                idx += 1
                cv2.imwrite(out_path,frame)
    #             skip 10 frame
                for i in range(10):
                    ret, frame = cap.read()
                    pbar.update(1)
    print 'Cropping : Done'











# 館長
video_path = join('./','buf_data','fit_coach1.mp4')
skip_beg_frame = 0 
fixed_size = 500
factor = None

# demo(video_path, constraint=None, return_max_area_face=True, factor=factor, fixed_size=fixed_size, skip_beg_frame=skip_beg_frame)
ouptut_path = join('./','buf_data','fit_coach')
crop_video(video_path, ouptut_path, constraint=None, return_max_area_face=True, factor=None, fixed_size=fixed_size, skip_beg_frame=skip_beg_frame)








