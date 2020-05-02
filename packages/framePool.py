import cv2
import numpy
from os import remove
import time


def createFramePool():
    pool = []
    return pool


def appendFrame(cap, pool):
    ret, frame = cap.read()
    fileName = numpy.random.randint(100000, 999999, 1)
    cv2.imwrite('./cache/' + str(fileName[0]) + '.jpg', frame)
    pool.append(fileName[0])
    return pool


def dropFrame(pool):
    if len(pool):
        remove('./cache/' + str(pool[0]) + '.jpg')
        fileName = pool.pop(0)
    return fileName, pool


if __name__ == '__main__':
    pool = createFramePool()
    cap = cv2.VideoCapture(0)
    cap.set(3, 960)
    cap.set(4, 540)
    for i in range(30):
        pool = appendFrame(cap, pool)
    print(pool)
    for i in range(300):
        pool = dropFrame(pool)
    print(pool)
    cap.release()
