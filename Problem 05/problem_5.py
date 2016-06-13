__author__ = 'Suvojit Manna'

#Write a program to covert grayscale image into binary image varying different threshold values.
#(many output images will be produced for one input image for different threshold values)

import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("grey2.jpg",cv2.COLOR_BGR2GRAY)
cv2.imshow("Input",image)
thres_lvl = [0,63,127,190,255]
for thres in thres_lvl:
    ret,img = cv2.threshold(image,thres,255,cv2.THRESH_BINARY)
    cv2.imshow("Output"+str(thres),img)
cv2.waitKey(0)