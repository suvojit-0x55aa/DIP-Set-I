__author__ = 'Suvojit Manna'

#  Write a program to enhance a given image using min filter.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("CBoard.jpg", cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
kSize = 3
bSize = kSize // 2 
image = cv2.copyMakeBorder(image, bSize, bSize, bSize, bSize, cv2.BORDER_CONSTANT, 0)
imageO = np.zeros(image.shape, dtype=np.uint8)
for x in range(image.shape[0] - kSize + 1):
    for y in range(image.shape[1] - kSize + 1):
        imageO[x, y] = np.amin(image[x:x+kSize, y:y+kSize])
cv2.imshow("Output : Min Filter", imageO)
cv2.waitKey(0)
