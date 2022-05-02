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


def calculate_area(img, mask, color):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        contour_area = cv2.contourArea(contour)
        cv2.drawContours(img, [contour], -1, color, 2)

    try:
        return contour_area
    except:
        pass


def draw_contours(img, mask, area):
    count = 0

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        contour_area = cv2.contourArea(contour)

        try:
            if area * 0.8 < contour_area < area * 1.2:
                cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
                count += 1
        except:
            pass

    return count


while True:

    _, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    result = frame.copy()

    obj_window = [(100, 100), (200, 200)]
    obj_color = (255, 0, 255)

    obj = select_object(obj_window, obj_color)
    obj_mask = create_mask(obj)
    obj_area = calculate_area(obj, obj_mask, obj_color)

    mask = create_mask(frame)
    count = draw_contours(result, mask, obj_area)

    cv2.putText(result, str(1), (obj_window[0][0] + 5, obj_window[0][1] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(result, str(count), (obj_window[0][0] + 5, obj_window[1][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

    cv2.imshow('result', result)
    # cv2.imshow('mask', obj_mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
