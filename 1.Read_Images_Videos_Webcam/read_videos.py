import cv2

cap = cv2.VideoCapture(r"C:\Users\Lovely\Desktop\Open_CV\Resources\marmots_family_animals_furry_cute_968.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
         break