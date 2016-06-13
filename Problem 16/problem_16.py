__author__ = 'Suvojit Manna'

#  Write a program to enhance a given image using max filter.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("CBoard.jpg", cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT, 0)
imageO = np.zeros(image.shape, dtype=np.uint8)
kSize = 3
for x in range(image.shape[0] - kSize + 1):
    for y in range(image.shape[1] - kSize + 1):
        imageO[x, y] = np.amax(image[x:x+kSize, y:y+kSize])
cv2.imshow("Output : Max Filter", imageO)
cv2.waitKey(0)