import cv2
import numpy as np

img = cv2.imread("Source/iskambil.jpg")

width,height = 300,200

pts1 = np.float32([[295,207],[470,203],[272,482],[473,478]]) # Fotoğraf üzerindeki belirli bir bölgeyi kırptık.
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("photo",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)