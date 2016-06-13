__author__ = 'Suvojit Manna'

# Write a program to enhance the image using unsharp masking and High-boost filtering.

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("eye.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)
gauss_mask = cv2.GaussianBlur(image, (9, 9), 10.0)
image_sharp = cv2.addWeighted(image, 2, gauss_mask, -1, 0)
# equivalent expr
#image = (image*1.5) - (gauss_mask*0.5)     # may produce artifact due to lack of saturation maths
cv2.imshow("Output : Sharpen", image_sharp)
#High pass Kernel 3x3
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
#High Pass Kernel 5x5
'''kernel = np.array([[-1, -1, -1, -1, -1],
                   [-1,  1,  2,  1, -1],
                   [-1,  2,  4,  2, -1],
                   [-1,  1,  2,  1, -1],
                   [-1, -1, -1, -1, -1]])'''

# Note
# High Pass Filters can also be obtained by subtracting a low pass filtered image
# from original image
# Using a LPF like Gaussian Filter
# image_hpf = image - gauss_mask

image_hpf = cv2.filter2D(image, -1, kernel)
cv2.imshow("Output : High Pass Filter", image_hpf)
cv2.waitKey(0)