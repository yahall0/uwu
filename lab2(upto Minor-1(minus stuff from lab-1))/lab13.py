import cv2
import numpy as np

img = cv2.imread('lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg', cv2.IMREAD_GRAYSCALE)

img_float32 = np.float32(img)

c = 255 / np.log(1 + np.max(img_float32))
log_transformed = c * np.log(1 + img_float32)

log_transformed = np.uint8(cv2.normalize(log_transformed, None, 0, 255, cv2.NORM_MINMAX))

gamma = 1.5
c = 255 / (np.max(img) ** gamma)
gamma_transformed = c * img**gamma

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Log", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gamma", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Original", 1366, 768)
cv2.resizeWindow("Log", 1366, 768)
cv2.resizeWindow("Gamma", 1366, 768)


cv2.imshow('Original', img)
cv2.imshow('Log', log_transformed)
cv2.imshow('Gamma', gamma_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
