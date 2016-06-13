__author__ = 'Suvojit Manna'

#Write a program to enhance the low contrast image to high contrast image using linear stretching method.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Hawkes.jpg",cv2.COLOR_BGR2GRAY)
minPix = np.amin(image)
maxPix = np.amax(image)
cv2.imshow("Input", image)
image -= minPix
image *= (255/(maxPix - minPix))
cv2.imshow("Output", image)
cv2.waitKey(0)