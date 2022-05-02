import cv2
import numpy as np

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)


def select_object(window, color):
    cv2.rectangle(result, window[0], window[1], color, 2, cv2.LINE_AA)
    obj = frame[window[0][1]:window[1][1], window[0][0]:window[1][0]]
    return obj


def create_mask(img):
    saturation = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)[:, :, 1]
    blur = cv2.GaussianBlur(saturation, (3, 3), 0)
    thresh = 255 - cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(thresh, kernel, iterations=1)
    return mask


while True:

    _, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    result = frame.copy()

    obj_window = [(100, 100), (200, 200)]
    obj_color = (255, 0, 255)

    obj = select_object(obj_window, obj_color)
    obj_mask = create_mask(obj)

    cv2.imshow('result', result)
    cv2.imshow('mask', obj_mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
