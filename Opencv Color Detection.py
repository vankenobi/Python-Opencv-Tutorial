import cv2
import numpy as np 

def empty():
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",300,300)

cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",0,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",0,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,179,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

path = "Source/photo1.jpg"

while True:
    img = cv2.imread(path)
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    v_max = cv2.getTrackbarPos("Val Max","Trackbars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Default Photo",img)
    cv2.imshow("Photo of HSV,",imgHsv)
    cv2.imshow("Mask",mask)
    cv2.imshow("image Result",imgResult)
    cv2.waitKey(1)

