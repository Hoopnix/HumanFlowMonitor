from cv2 import HOGDescriptor, HOGDescriptor_getDefaultPeopleDetector, rectangle
from numpy import array
from imutils.object_detection import non_max_suppression
import torchvision
from torch import load


def hogSvmDetector(frame, num):
    flag = 0
    defaultHog = HOGDescriptor()
    defaultHog.setSVMDetector(HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = defaultHog.detectMultiScale(frame, winStride=(4, 4), padding=(16, 16), scale=1.02)
    rects = array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    for (xA, yA, xB, yB) in pick:
        rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        centre_x = int((xA + xB) / 2)
        if 170 >= centre_x >= 150:
            flag += 1
            if flag >= 3:
                flag = 0
                num += 1
    return num, frame


def fasterRCNNDetector(frame, line):
    pass


def fasterRCNNInit():
    pass


if __name__ == '__main__':
    pass
    from PIL import Image

    img = Image.open('../a.jpg')
    Image._show(img)
