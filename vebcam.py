import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    cv2.rectangle(frame, (10, 10), (300, 200), (0, 255, 0), 3)
    cv2.putText(frame, 'Hello World', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("data", frame)

    if cv2.waitKey(1) == ord(" "):
        break

cap.release()
cv2.destroyAllWindows()