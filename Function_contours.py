import cv2  
  
img = cv2.imread('triangle.png')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
  
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  

cnt = contours[1]

#print(cnt)

perimeter = cv2.arcLength(cnt,True) # 計算周長
print(perimeter)

cv2.drawContours(img,contours,1,(255,0,0),4)  

  
cv2.imshow("img", img)  
cv2.waitKey(0) 
