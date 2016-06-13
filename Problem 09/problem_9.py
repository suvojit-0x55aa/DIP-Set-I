__author__ = 'Suvojit Manna'

#Write a program to find the histogram of a image and then plot the histogram.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('eye.jpg',cv2.COLOR_BGR2GRAY)
cv2.imshow("Input",image)
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY )
plt.hist(image.ravel(),256,[0,256]); plt.show()
cv2.waitKey(0)