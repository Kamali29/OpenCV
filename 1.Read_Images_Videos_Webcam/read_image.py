import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread(r"C:\Users\Lovely\Desktop\Open_CV\Resources\lena.png",0)
# DISPLAY
print(img)
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()