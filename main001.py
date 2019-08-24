import cv2 as cv
import numpy as np
erosion_size = 0
max_elem = 2
max_kernel_size = 21

def erosion(val):
    erosion_type = 0
    erosion_size = 10
    element = cv.getStructuringElement(erosion_type, (2*erosion_size + 1, 2*erosion_size+1), (erosion_size, erosion_size))
    erosion_dst = cv.erode(src, element)
    cv.imshow(title_erosion_window, erosion_dst)

def dilatation(val):
    dilatation_type = 0
    element = cv.getStructuringElement(dilatation_type, (2*dilatation_size + 1, 2*dilatation_size+1), (dilatation_size, dilatation_size))
    dilatation_dst = cv.dilate(src, element)
    cv.imshow(title_dilatation_window, dilatation_dst)

if __name__=='main':
 
src = cv.imread() 
  









