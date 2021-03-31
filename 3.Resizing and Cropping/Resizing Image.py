import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Lovely\Desktop\Open_CV\Resources\lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.imshow("Image Resize",imgResize)
cv2.waitKey(0)
