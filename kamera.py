import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp2/weights/last.pt', force_reload=True)
import random
import uuid   # Unique identifier
import os
import time
import matplotlib.image as mpimg
IMAGES_PATH = os.path.join('yolov5','data', 'images') #/data/images
labels = ['coba']
number_imgs = 1
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    imgname = os.path.join(IMAGES_PATH,'coba.jpg')
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.imwrite(imgname, frame)
        results.print()
        results.save()
        break
cap.release()
cv2.destroyAllWindows()
results.xyxy
coor = results.xyxy[0]
rows = len(coor)
kiper = 1
gawang = 0
i = 0
j = 0
flagGK = 0
flagG = 0
diffx = 20
diffy = 10
invalid= 0
#gawang 
while i < rows:
    if coor[i][5].item() == gawang:
        XminG = coor[i][0].item()
        YminG = coor[i][1].item()
        XmaxG = coor[i][2].item()
        YmaxG = coor[i][3].item()
        print("Gawang Terdeteksi")
        flagG += 1
    i += 1

if flagG == 0:
    XminG = 0
    YminG = 0
    XmaxG = 640
    YmaxG = 480
    print("Gawang Tidak Terdeteksi")

lebarG = XmaxG - XminG
pos = lebarG / 3
XmidleftG = XminG + pos
XmidrightG = XmaxG - pos

while j < rows:
    if coor[j][5].item() == kiper:
        if coor[j][0].item() >= XminG and coor[j][2].item() <= XmaxG:
            XminGK = coor[j][0].item()
            YminGK = coor[j][1].item()
            XmaxGK = coor[j][2].item()
            YmaxGK = coor[j][3].item()
            print("Kiper Terdeteksi")
            flagGK += 1
    j += 1

if flagGK == 0:
    invalid = invalid + 1
    XminGK = XminG
    YminGK = YminG
    XmaxGK = XmaxG
    YmaxGK = YmaxG
    print("Kiper Tidak Terdeteksi")
    
if flagGK == 0 and flagGK == 0:
    invalid = invalid + 1
    print("Invalid")

if XmaxGK < XmidrightG and XminGK > XmidleftG:                  #kiper tengah
    ballx = np.random.uniform(XminG+diffx, XmaxG-diffx)
    bally = np.random.uniform(YminG+diffy, YmaxG-diffy)
    while ballx < XmidrightG+diffx and ballx > XmidleftG-diffx:
        ballx = np.random.uniform(XminG+diffx, XmaxG-diffx)
        bally = np.random.uniform(YminG+diffy, YmaxG-diffy)
    print("kiper di tengah")
    print("bola kanan / kiri")
elif XmaxGK < XmidleftG:                                        #kiper kiri
    ballx = np.random.uniform(XmidleftG+diffx, XmaxG-diffx)
    bally = np.random.uniform(YminG+diffy, YmaxG-diffy)
    print("bola kanan / tengah")
    print("kiper di kiri")
elif XmaxGK < XmidrightG:                                       #kiper tengah kiri  
    ballx = np.random.uniform(XmidrightG+diffx, XmaxG-diffx)
    bally = np.random.uniform(YminG+diffy, YmaxG-diffy)
    print("bola kanan")
    print("kiper di kiri tengah")
elif XminGK > XmidrightG:                                       #kiper kanan
    ballx = np.random.uniform(XminG+diffx, XmidrightG-diffx)
    bally = np.random.uniform(YminG+diffy, YmaxG-diffy)
    print("bola kiri / tengah")
    print("kiper di kanan")
elif XminGK > XmidleftG:                                       #kiper tengah kanan
    ballx = np.random.uniform(XminG+diffx, XmidleftG-diffx)
    bally = np.random.uniform(YminG+diffy, YmaxG-diffy)
    print("bola kiri")
    print("kiper di kanan tengah")
else:
    print("invalid kiper di 3 interval")
    invalid = invalid + 1

if invalid == 0:
    IMAGES_PATH1 = os.path.join('yolov5','data','images')
    imgres = os.path.join(IMAGES_PATH,labels[0]+'coba.jpg')
    # Reading an image in default mode
    image = cv2.imread('runs\detect\exp\image0.jpg')
    ballx = int(ballx)
    bally = int(bally)
    # Center coordinates
    center = (ballx, bally)
 
    # Radius of circle
    radius = 10
  
    # Red color in BGR
    color = (0, 0, 255)
  
    # Line thickness of -1 px
    thickness = -1
  
    # Using cv2.circle() method
    # Draw a circle of red color of thickness -1 px
    image = cv2.circle(image, center, radius, color, thickness)
    print(os.path.join(IMAGES_PATH, labels[0]+'.jpg'))
    # Writes out image to file 
    cv2.imwrite(imgres, image)
    # Displaying the image
    cv2.imshow('YOLO', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

IMAGES_PATH1 = os.path.join('runs','detect', 'exp')
os.remove("runs\detect\exp\image0.jpg")
os.rmdir("runs\detect\exp")
print("Berhasil reset")