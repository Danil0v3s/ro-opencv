import os
import cv2 as cv

def negative():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('negative'):
            f.write("negative/" + filename + "\n")

def positive():
    with open('pos.txt', 'w') as f:
        for filename in os.listdir('positive'):
            image = cv.imread('positive/{}'.format(filename), cv.IMREAD_UNCHANGED)
            f.write("positive/{} 1 0 0 {} {}\n".format(filename, image.shape[1], image.shape[0]))