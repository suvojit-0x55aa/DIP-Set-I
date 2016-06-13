__author__ = 'Suvojit Manna'

# Write a program to enhance the image using 1st order derivative filtering.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Bikesgray.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)

#Using 2nd order Laplacian Operator without Gaussian Filter
image1 = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=1)
image2 = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=1)
image1 = image1.astype(np.uint64)
image2 = image2.astype(np.uint64)
image = np.sqrt(np.power(image1, 2) + np.power(image2, 2))
cv2.imshow("Output : 1st Ord Derivative", image)
cv2.waitKey(0)