"""Gray level Slicing"""

import cv2
import numpy as np

img = cv2.imread('lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg', cv2.IMREAD_GRAYSCALE)

lower_bound = 60
upper_bound = 120

img_without_bg = np.where((img >= lower_bound) & (img <= upper_bound), 255, 0).astype(np.uint8)

img_with_bg = np.where((img >= lower_bound) & (img <= upper_bound), 255, img).astype(np.uint8)

cv2.namedWindow("Win1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Win2", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Win1", 1366, 768)
cv2.resizeWindow("Win2", 1366, 768)


cv2.imshow('Win1', img_without_bg)
cv2.imshow('Win2', img_with_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()
