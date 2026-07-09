#Import 
import cv2

phone_ip = "http://192.168.234.71:8080/video"
cap = cv2.VideoCapture(phone_ip)

while True:

    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyWindow()