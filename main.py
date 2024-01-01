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

    processed_image = vision.apply_hsv_filter(screenshot)
    rectangles = vision.find(processed_image, 0.5)
    output_image = vision.draw_rectangles(screenshot, rectangles)

    cv.imshow('Processed', processed_image)
    cv.imshow('Matches', output_image)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('Done')