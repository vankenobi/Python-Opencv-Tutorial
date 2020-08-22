import cv2
import numpy as np 

kernel = np.ones((3,3),np.uint8)

img = cv2.imread("Source/photo.jpg")                # Normal Görüntü
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)      # Gri Tonlamalı Görüntü
imgBlur = cv2.GaussianBlur(img,(7,7),0)             # Blurlu Görüntü 
imgCanny = cv2.Canny(img,150,150)                   # Kenarları belirginleştirilmiş görüntü
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)  # Kenarları belirginleştirip kalınlaştırılmış görüntü
imgEroded = cv2.erode(img,kernel,iterations=1)      # Aşınmış bir görüntü


cv2.imshow("Default Photo",img)
cv2.imshow("Gray Photo",imgGray)
cv2.imshow("Blur Photo",imgBlur)
cv2.imshow("Canny Photo",imgCanny)
cv2.imshow("Dilation Photo",imgDilation)
cv2.imshow("Erode Photo",imgEroded)

cv2.waitKey(0)