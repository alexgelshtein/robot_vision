import cv2.cv2 as cv2
import numpy as np

def detect(number):
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FPS, 24)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    template = cv2.imread('images/opencv_frame_cropped_{}.png'.format(number),0)
    w, h = template.shape[::-1]

    while True:
        _ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("camera", gray)
        if cv2.waitKey(10) == 27:
            break
        
        res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8

        loc = np.where(res >= threshold)
        s = loc[0].size

        if s != 0:
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

            cv2.imshow('Detected',img)
            # cv2.waitKey(0)
            print('Detected!')
            break

    cap.release()
    cv2.destroyAllWindows()

# detect(0)