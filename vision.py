import cv2 as cv
import numpy as np

class Vision:

    needle_img = None
    needle_h = 0
    needle_w = 0
    method = None

    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
        
        self.needle_h = self.needle_img.shape[0]
        self.needle_w = self.needle_img.shape[1]

        self.method = method

    def find(self, haystack_img, threshold = 0.7, debug_mode=None):
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        # create cv rectangles of [x,y,w,h]
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
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

        return points
