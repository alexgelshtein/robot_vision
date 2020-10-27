import cv2.cv2 as cv2
import numpy as np

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        cv2.destroyAllWindows()
        x, y, w, h = map(int, input().split())
        crop_img_name = "images/opencv_frame_cropped_0.png"
        crop_frame = frame[y:y+h, x:x+w]
        cv2.imwrite(crop_img_name, crop_frame)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,255), 2)
        cv2.imshow("Ok?", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Written!")

cam.release()
cv2.destroyAllWindows()