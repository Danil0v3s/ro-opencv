import cv2 as cv
import numpy as np
import pyautogui
from time import time
from windowcapture import WindowCapture


def find_click_positions(needle_img_path, haystack_img_path, threshold = 0.7, debug_mode=None):
    haystack_img = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)
    needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

    needle_h = needle_img.shape[0]
    needle_w = needle_img.shape[1]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack_img, needle_img, method)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    # create cv rectangles of [x,y,w,h]
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        # duplicate so groupRectangles doesnt discard a single rect
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    points = []

    if len(rectangles):
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255,0,255)
        marker_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:
            # center of the rectangle
            center_x = x + int(w/2)
            center_y = y + int(h/2)

            points.append((center_x, center_y))

            if debug_mode == 'rect':
                top_left = (x,y)
                bottom_right = (x + w, y + h)
                cv.rectangle(haystack_img, top_left, bottom_right, line_color, 1, line_type)
            elif debug_mode == 'cross':
                cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

        if debug_mode:
            cv.imshow("Result", haystack_img)
            cv.waitKey()

    return points


wincap = WindowCapture("4th | Gepard Shield 3.0 (^-_-^)")

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()

    cv.imshow("CV", screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('Done')