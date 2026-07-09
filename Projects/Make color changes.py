#Import 
import cv2

phone_ip = "your ip"
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyWindow()