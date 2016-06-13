__author__ = 'Suvojit Manna'

# Write a program in MATLAB to enhance the image using Robert Operator.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Bikesgray.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)

# Robert Cross operators
kernelV = np.array([[1,  0],
                   [0,  -1]])
kernelH = np.array([[1,  0],
                   [0,  -1]])

image1 = cv2.filter2D(image, -1, kernelV)
image2 = cv2.filter2D(image, -1, kernelH)
image1 = image1.astype(np.uint64)
image2 = image2.astype(np.uint64)
image = np.sqrt(np.power(image1,2) + np.power(image2,2))
image = image.astype(np.uint8)
cv2.imshow("Output : Robert Ops", image)
cv2.waitKey(0)