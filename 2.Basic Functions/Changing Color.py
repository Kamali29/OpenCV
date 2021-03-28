import cv2

# Method1
img = cv2.imread(r"C:\Users\Lovely\Desktop\Open_CV\Resources\lena.png")
img1 = cv2.imread(r"C:\Users\Lovely\Desktop\Open_CV\Resources\lena.png",0)

cv2.imshow('colored Image',img)
cv2.waitKey(0)
cv2.imshow('Gray Image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Method2
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('colored Image',img)
cv2.waitKey(0)
cv2.imshow('Gray Image',imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()