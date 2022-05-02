import cv2

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)


def select_object(window, color):
    cv2.rectangle(result, window[0], window[1], color, 2, cv2.LINE_AA)
    obj = frame[window[0][1]:window[1][1], window[0][0]:window[1][0]]
    return obj


while True:

    _, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    result = frame.copy()

    obj_window = [(100, 100), (200, 200)]
    obj_color = (255, 0, 255)

    obj = select_object(obj_window, obj_color)

    cv2.imshow('result', result)
    cv2.imshow('object', obj)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
