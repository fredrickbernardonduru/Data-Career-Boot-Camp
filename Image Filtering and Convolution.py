import cv2
import numpy as np


# Read an image
image = cv2.imread('C:\\Users\\Fredrich Bernard\\Downloads\\IMG_1556.jpg')



#Define a blur filter kernel (3x3)

kernel = np.ones((3, 3), np.float32) / 9

#Apply convolutional using OpenCV's filter2D function
filtered_image = cv2.filter2D(image, -1, kernel)

#Display original and filtered images
cv2.imshow('Original Images', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()