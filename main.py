import cv2 as cv
import numpy as np
import win32api, win32con

from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision
from detection import Detection
from bot import RagBot, BotState

wincap = WindowCapture("4th | Gepard Shield 3.0 (^-_-^)")
vision = Vision(None)
detector = Detection('cascade/cascade.xml')
bot = RagBot(window_offset=(wincap.offset_x, wincap.offset_y), window_size=(wincap.w, wincap.h))

DEBUG = True

def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def bot_actions(rectangles):
    if len(rectangles) > 0:
        targets = vision.get_click_points(rectangles)
        target = wincap.get_screen_position(targets[0])
        click(x=target[0], y=target[1])

    global is_bot_in_action
    is_bot_in_action = False

wincap.start()
detector.start()
bot.start()

loop_time = time()
while(True):
    if wincap.screenshot is None:
        continue

    detector.update(wincap.screenshot)

    if (bot.state == BotState.INITIALIZING):
        targets = vision.get_click_points(detector.rectangles)
        bot.update_targets(targets)
    
    if DEBUG:
        detection_image = vision.draw_rectangles(wincap.screenshot, detector.rectangles)
        fps = int(1 / (time() - loop_time))
        cv.putText(detection_image, 'FPS {}'.format(fps), (10,50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 1, cv.LINE_AA)
        cv.imshow('Matches', detection_image)

    loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        detector.stop()
        wincap.stop()
        bot.stop()
        cv.destroyAllWindows()
        break
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(time()), wincap.screenshot)
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(time()), wincap.screenshot)

print('Done')