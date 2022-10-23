# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:53:00 2022

@author: cakir
"""

import cv2
import torch
from time import time
import numpy as np
import pytesseract
from CropImage import cropImage
import threading

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

model = torch.hub.load('', 'custom', path='best1500.pt', source='local')

cap = cv2.VideoCapture("PexelsVideos2103099.mp4")

cv2.namedWindow("output", cv2.WINDOW_NORMAL) 


ret, frame = cap.read()
x, y = frame.shape[:2]
value = np.array([
        [(x * 0.2, x),#SOL ALT NOKTA
        ((int((y * 3.2) / 20)), int(x * 0.75)), #SOL ÜST NOKTA
        (int((y * 5 ) / 5.8), int(x * 0.75)), #SAĞ ÜST NOKTA
        (y * 0.9, x)]], np.int32)

def plate(point):
    x = int(point[2])
    
    y = int(point[3]) #Burdaki (x, y) koordinati sağ alt köşeyi veriyor unutma!
    
    w = int(point[2] - point[0]) #genişlik bulma xmax - xmin
    
    h = int(point[3] - point[1]) #yükseklik bulma ymax - ymin
                    
    roi = frame[y - h + 10 : y - 5, x - w + 35 : x - 30]
                    
    _, treshold_image = cv2.threshold(roi, 75, 255, cv2.THRESH_TOZERO)
                    
    plate = pytesseract.image_to_string(treshold_image,lang = "eng")
                    
    print(plate)
    

loop_time = time()
while cap.isOpened():
    _, frame = cap.read()
    
    screen = frame.copy()
             
    #-------------CropImage Kısmı--------------
    croppedImage = cropImage(frame)
    
    matris = croppedImage.corpSize()
    
    frame = croppedImage.crop_image(matris)
    #------------------------------------------
    
    results = model(frame)
    
    points = results.xyxy[0].tolist()
    
    try:
        #xmax ve ymax noktaları
        t1 = threading.Thread(target=plate, args = (points[0],))
        t1.start()
        if len(points) == 2:
            t2 = threading.Thread(target=plate, args = (points[1],))
            t2.start()

    except IndexError:
        pass
    
    cv2.polylines(screen, [value], True, (0,0,255), 3)
        
    #screen[0:500,0:900] = cv2.resize(results.render()[0], (900, 500))
                                     
    cv2.imshow('output', screen)
    #cv2.imshow('output', results.render()[0])

    
    print("fps {}".format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()