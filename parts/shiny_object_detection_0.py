import cv2

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

while True:

    _, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    result = frame.copy()

    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
