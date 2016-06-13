__author__ = 'Suvojit Manna'

#Write a program to remove the impulsive noise using median filtering technique.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("noisy.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
image = cv2.medianBlur(image, 5)
cv2.imshow("Output", image)
cv2.waitKey(0)