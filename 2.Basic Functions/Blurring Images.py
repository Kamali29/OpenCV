# Image Blurring
# Image Blurring refers to making the image less clear or distinct. It is done with the help of various
# low pass filter kernels.

# Advantages of blurring:
# 1.It helps in Noise removal. As noise is considered as high pass signal so by the application of low pass filter
#   kernel we restrict noise.
# 2.It helps in hiding the details when necessary. For e.g. in many cases police deliberately want to hide the face
#   of the victim, in such cases blurring is required.

# Important types of blurring:
# Gaussian Blurring
# Median Blur
# Bilateral Blur

import cv2

img = cv2.imread(r"C:\Users\Lovely\Desktop\Open_CV\Resources\lena.png")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_Gaussian_Blur = cv2.GaussianBlur(imgGray,(7,7),0)
img_Median_Blur = cv2.medianBlur(imgGray, 5)
img_Bilateral_Blur = cv2.bilateralFilter(imgGray, 9, 75, 75)

cv2.imshow('colored Image',img)
cv2.waitKey(0)
cv2.imshow('Gray Image',imgGray)
cv2.waitKey(0)
cv2.imshow('Gaussian Blurred Image',img_Gaussian_Blur)
cv2.waitKey(0)
cv2.imshow('Median Blurred Image',img_Median_Blur)
cv2.waitKey(0)
cv2.imshow('Bilateral Blurred Image',img_Bilateral_Blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
