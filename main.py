import cv2 as cv
import numpy as np

haystack_img = cv.imread('images/screen.png', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('images/toad.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

threshold = 0.8
if max_val > threshold:
    print('found')
    
    needle_h = needle_img.shape[0]
    needle_w = needle_img.shape[1]

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
    cv.imshow('Result', haystack_img)
    cv.waitKey()
else:
    print('not found')