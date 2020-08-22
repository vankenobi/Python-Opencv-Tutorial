import cv2
import numpy as np 

img = np.zeros((200,200,3),np.uint8) # 200px * 200px lik 3 renk kanalına sahip bir fotoğraf elde ettik.
img[0:50,100:150] = 255,0,0          # Çıkan fotoğraftaki boyalı alanın sadece belirli kısmını maviye boyadık.
cv2.line(img,(0,0),(200,50),(0,0,255),thickness=3) # Çıkan fotoğraf üzerine bir çizgi çizdik.
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # Fotoğrafın köşegeni boyunca bir çizgi çizdirdik.
cv2.rectangle(img,(30,30),(100,100),(0,0,255),cv2.FILLED) # Bir dikdörtgen çizdirdik içinin dolu olmasını istemiyorsak CV2.FILLED kaldırılabilir.
cv2.circle(img,(150,150),30,(255,0,0),thickness=3)  # Bir çember oluşturduk merkezi x=150 y=150 olan rengi = mavi kalınlığıda = 2 
cv2.putText(img,"OpenCv",(0,150),cv2.FONT_HERSHEY_COMPLEX,0.75,(255,0,0),thickness=2)

cv2.imshow("image",img)



cv2.waitKey(0)