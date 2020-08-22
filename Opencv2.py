import cv2

cap = cv2.VideoCapture(0)
cap.set(3,200) # Width id = 3           Value = 200
cap.set(4,250) # Height id = 4          Value = 250 
cap.set(10,100) # Brightness id = 10    Value = 100

while True:
    success , img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break