import cv2.cv2 as cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 24)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # flip = cv2.flip(gray, 1)
    cv2.imshow("camera", gray)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()