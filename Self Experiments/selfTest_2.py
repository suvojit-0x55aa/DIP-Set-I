__author__ = 'Suvojit Manna'

#  Write a program to enhance the image using Sobel-Feldman Operator.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Bikesgray.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)

# Sobel-Feldman Operators
kernelV = np.array([[-3, -10, -3],
                   [0, 0, 0],
                   [3, 10, 3]])
kernelH = np.array([[-3, 0, 3],
                   [-10, 0, 10],
                   [-3, 0, 3]])

image1 = cv2.filter2D(image, -1, kernelV)
image2 = cv2.filter2D(image, -1, kernelH)
image1 = image1.astype(np.uint64)
image2 = image2.astype(np.uint64)
image = np.sqrt(np.power(image1,2) + np.power(image2,2))
image = image.astype(np.uint8)
cv2.imshow("Output : Sobel-Feldman Ops", image)
cv2.waitKey(0)
