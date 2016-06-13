__author__ = 'Suvojit Manna'

# Write a program to remove the noise using weighted averaging filtering technique from noisy image.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("noisy.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input",image)
kernel = np.ones((5,5),dtype=np.float32)
kernel[3, 3] = 10.0
kernel /= 34
image = cv2.filter2D(image,-1,kernel)
cv2.imshow("Output",image)
cv2.waitKey(0)