# Dilation adds pixels to the boundaries of objects in an image,
# while erosion removes pixels on object boundaries.
#  It is normally performed on binary images.

import cv2
import numpy as np

# Reading the input image
img = cv2.imread(r'C:\Users\Lovely\Desktop\Open_CV\Resources\lena.png', 0)

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5, 5), np.uint8)

imgCanny = cv2.Canny(img,150,200)

img_dilation = cv2.dilate(imgCanny, kernel, iterations=1)
img_erosion = cv2.erode(img_dilation, kernel, iterations=1)


cv2.imshow('Input', img)

cv2.waitKey(0)
cv2.imshow('Canny Image', imgCanny)
cv2.waitKey(0)
cv2.imshow('Eroded Image', img_erosion)
cv2.waitKey(0)
cv2.imshow('Dilated Image', img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()