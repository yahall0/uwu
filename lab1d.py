# import cv2
# import numpy as np

# img = cv2.imread("T-90M.jpg")

# img_mod = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)

# cv2.imshow("Orig", img)
# cv2.imshow("T-90M.jpg", img_mod)

# cv2.waitKey(0)

from email.mime import image
import sklearn
from skimage import color
from skimage import io, transform
from matplotlib import pyplot as plt

img = io.imread("T-72B3.jpg")

img_mod = transform.rescale(img, 0.25);
img_mod_anti = transform.resize(img, 0.25, anti_alialiasing=True)

plt.imshow(img_mod)
plt.imshow(img_mod_anti)
plt.show()

