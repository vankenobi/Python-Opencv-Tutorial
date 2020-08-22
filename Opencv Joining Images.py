import cv2 
import numpy as np
 
img = cv2.imread("Source/photo.jpg")

horImg = np.hstack((img,img)) 
verImg = np.vstack((img,img))
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("horizantol duplicate image",horImg) # Yatay ikileme
cv2.imshow("Vertical duplicate image",verImg) # Dikey ikileme
cv2.imshow("HSV image",imgHSV) # HSV li görüntü

cv2.waitKey(0)