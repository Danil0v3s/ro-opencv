import cv2 as cv
import numpy as np

class Vision:

    needle_img = None
    needle_h = 0
    needle_w = 0
    method = None

    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        if needle_img_path:
            self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
            
            self.needle_h = self.needle_img.shape[0]
            self.needle_w = self.needle_img.shape[1]

        self.method = method

    def get_click_points(self, rectangles):
        points = []

        if len(rectangles):

            for (x, y, w, h) in rectangles:
                # center of the rectangle
                center_x = x + int(w/2)
                center_y = y + int(h/2)

                points.append((center_x, center_y))
            
            return points
        
    def draw_rectangles(self, haystack_img, rectangles):
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            top_left = (x,y)
            bottom_right = (x + w, y + h)
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, 1, line_type)

        return haystack_img

    def draw_marker(self, haystack_img, points):
        marker_color = (255,0,255)
        marker_type = cv.MARKER_CROSS

        for point in points:
            cv.drawMarker(haystack_img, point, marker_color, marker_type)

        return haystack_img
        if amount > 0:
            lim = 255 - amount
            c[c >= lim] = 255
            c[c < lim] += amount
        elif amount < 0:
            amount = -amount
            lim = amount
            c[c <= lim] = 0
            c[c > lim] -= amount
        return c