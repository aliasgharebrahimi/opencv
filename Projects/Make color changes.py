#Import 
import cv2

phone_ip = "your ip"
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyWindow()