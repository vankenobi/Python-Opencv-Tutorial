import cv2
import numpy as np 

img = cv2.imread("Source/photo.jpg")
cv2.imshow("Default Photo",img)

print(img.shape)                        # Fotoğrafın boyutunu öğrenmek için kullanılır.

imgResize = cv2.resize(img,(300,200))   # Ana Fotoğrafımızı tekrardan boyutlandırdık.
imgResize2 = cv2.resize(img,(1000,700)) 

imgCropped = img[100:300,100:500]       #İnce bir nokta önce yükseklik değeri giriliyor. [Height,width]

cv2.imshow("imgResize Photo",imgResize)
cv2.imshow("imgResize Big Photo",imgResize2)
cv2.imshow("Cropped Photo",imgCropped)


cv2.waitKey(0)