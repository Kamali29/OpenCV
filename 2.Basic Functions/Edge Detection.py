import cv2

img = cv2.imread(r"C:\Users\Lovely\Desktop\Open_CV\Resources\lena.png")

imgCanny = cv2.Canny(img,150,200)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.imshow('Canny Image',imgCanny)
cv2.waitKey(0)
