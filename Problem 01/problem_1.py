__author__ = 'Suvojit Manna'

#Write a program to read a given binary image and convert it into its negative image.

import cv2
#from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("binary500.jpg")
cv2.imshow("Input",image)
out_image = 255 - image
cv2.imshow("Output",out_image)
cv2.waitKey(0)