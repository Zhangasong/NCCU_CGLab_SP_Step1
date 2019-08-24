# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:48:12 2019
@author: Zhangyusong

"""
import cv2
import numpy as np
import argparse

"""Read input file"""
parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
parser.add_argument('--input', help='Path to input image.', default='LinuxLogo.jpg')
args = parser.parse_args()
src = cv2.imread(cv2.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

"""Do gaussian thresholding
grayscaled = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY) 
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('gaus',gaus)
"""

"""Polygon Canvas"""
canvas = np.zeros((500,500,3),np.uint8)
canvas.fill(255)

kernel_size = 20
for i in range(15):

   """Do erodsion"""

   kernel = np.ones((kernel_size,kernel_size),np.uint8)
   dilation = cv2.dilate(src,kernel,iterations = 1)
   
   
   """Find contours"""    
   
   gray = cv2.cvtColor(dilation,cv2.COLOR_BGR2GRAY)  
   ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
   contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   

   """Draw contours"""
   cnt = contours[1]
   print(cnt)
   perimeter = cv2.arcLength(cnt,True) # 計算周長
   print("This round perimeter is ",perimeter)
   cv2.polylines(canvas,[cnt],True,(255,0,0),1)

   kernel_size+=5



cv2.imshow('Canvas',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


