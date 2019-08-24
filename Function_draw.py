import numpy as np
import cv2

img = np.zeros((1000,1000,3),np.uint8)
img.fill(255)

pts = np.array([[170,55],[165,75],[220,100],[400,60]],np.int32)

cv2.polylines(img,[pts],True,(255,255,0),4)


cv2.imshow('My_Image',img)
cv2.waitKey(0)
cv2.destoryAllWindows()
