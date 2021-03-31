import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Lovely\Desktop\Open_CV\Resources\lambo.png")
print(img.shape)


imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)