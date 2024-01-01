import cv2 as cv
import numpy as np
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture("4th | Gepard Shield 3.0 (^-_-^)")
vision = Vision('images/toad.jpg')

loop_time = time()
while(True):
    screenshot = wincap.get_screenshot()

    points = vision.find(screenshot, 0.5, debug_mode='rect')

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('Done')