import cv2
import numpy as np

img = cv2.imread('triangle.png')

#retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWinows()


