__author__ = 'Suvojit Manna'

#Write a program to apply log transformation on grayscale images.

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("eye.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
c = 15
image = image.astype(np.uint64)
image_o = c*np.log2(np.where(image >= 255, image, image+1))
image_o = image_o.astype(np.uint8)
cv2.imshow("Output", image_o)
cv2.waitKey(0)