import cv2 as cv
import numpy as np
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture("4th | Gepard Shield 3.0 (^-_-^)")
cascade = cv.CascadeClassifier('cascade/cascade.xml')
vision = Vision(None)

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()
    rectangles = cascade.detectMultiScale(screenshot)
    
    detection_image = vision.draw_rectangles(screenshot, rectangles)

    cv.imshow('Matches', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)

print('Done')