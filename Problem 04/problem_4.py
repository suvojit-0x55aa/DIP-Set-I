__author__ = 'Suvojit Manna'

#Write a program to apply power law transformation on a grayscale image varying parameter range to produced different output images for the same input image.

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("eye.jpg",cv2.COLOR_BGR2GRAY)
cv2.imshow("Input",image)
image = image.astype(np.uint64)
c=6
gamma = [0.05, 0.2, 0.67, 1.5, 2.5]
for g in gamma:
    img = c*np.power(image,g)
    img = img.astype(np.uint8)
    cv2.imshow("Output="+str(g),+img)
cv2.waitKey(0)