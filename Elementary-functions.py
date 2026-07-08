#Imports
import cv2

# Reading the image
img_pytoch = cv2.imread("images.jfif")

# Color transformations
gray = cv2.cvtColor(img_pytoch, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img_pytoch, cv2.COLOR_BGR2HSV)      
rgb = cv2.cvtColor(img_pytoch, cv2.COLOR_BGR2RGB) 

resized = cv2.resize(img_pytoch, (400, 300))  
cropped = img_pytoch[50:200, 100:300]   

cv2.rectangle(img_pytoch, (100, 100), (300, 200), (0, 255, 0), 2)
cv2.circle(img_pytoch, (100,100), 50, (0,0,255), 3)
cv2.putText(img_pytoch, 'Hello', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#View photo
cv2.imshow("logo pytorch", img_pytoch)

#Time to close the photo
cv2.waitKey(0)
#Close all windows
cv2.destroyAllWindows()