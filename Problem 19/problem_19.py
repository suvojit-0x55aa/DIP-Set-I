__author__ = 'Suvojit Manna'

# Write a program to enhance the image using 2nd order derivative filtering.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Bikesgray.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
#Using 2nd order Laplacian Operator without Gaussian Filter
imageWob = cv2.Laplacian(image, cv2.CV_64F,ksize=1)
cv2.imshow("Output : 2nd Ord Derivative w/o Blur",imageWob)
#Using Gaussian Filter to remove Noise
image = cv2.GaussianBlur(image, (3, 3), 5.0)  # remove noise with Gaussian blur
image = cv2.Laplacian(image, cv2.CV_64F, ksize=1)
cv2.imshow("Output : 2nd Ord Derivative", image)
cv2.waitKey(0)