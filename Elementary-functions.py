#Imports
import cv2

# Reading the image
img_pytoch = cv2.imread("images.jfif")

#View photo
cv2.imshow("logo pytorch", img_pytoch)

#Time to close the photo
cv2.waitKey(0)

#Close all windows
cv2.destroyAllWindows()