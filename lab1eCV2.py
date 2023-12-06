import cv2
import numpy as np

img = cv2.imread('T-90M.jpg')

blue,green,red = cv2.split(img)

zeros = np.zeros(blue.shape, np.uint8)

blueBGR = cv2.merge([blue,zeros,zeros])
greenBGR = cv2.merge([zeros,green,zeros])
redBGR = cv2.merge([zeros,zeros,red])


cv2.namedWindow('Blue Channel')
cv2.moveWindow('Blue Channel', 0, 0)
cv2.imshow('Blue Channel', blueBGR)

cv2.namedWindow('Green Channel')
cv2.moveWindow('Green Channel', blueBGR.shape[1], 0)
cv2.imshow('Green Channel', greenBGR)

cv2.namedWindow('Red Channel')
cv2.moveWindow('Red Channel', blueBGR.shape[1] * 2, 0)
cv2.imshow('Red Channel', redBGR)

cv2.waitKey(0)
cv2.destroyAllWindows()