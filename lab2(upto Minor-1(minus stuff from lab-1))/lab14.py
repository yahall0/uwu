from asyncio import windows_events
import cv2
import numpy as np

img = cv2.imread('lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg')

levels = [2, 4, 8, 16, 32]

for level in levels:
    quantized_img = np.floor(img / 256 * level) * (256 / level)

    quantized_img = np.uint8(quantized_img)

    window_name = f'Quantized Image - {level} Levels'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1366, 768)
    cv2.imshow(window_name, quantized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
