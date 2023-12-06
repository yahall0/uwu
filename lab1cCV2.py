

import cv2
import numpy as np

img = cv2.imread("T-90M.jpg")

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




cv2.imshow("T-90M.jpg", img_grey)


cv2.waitKey(0)
