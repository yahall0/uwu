import numpy as np

import sklearn
from skimage import color
from skimage import io
from matplotlib import pyplot as plt

img = io.imread("T-72B3.jpg")

imgR = img[:, :, 0]
imgG = img[:, :, 1]
imgB = img[:, :, 2]

imgR_colored = np.zeros_like(img)
imgR_colored[:, :, 0] = imgR

imgG_colored = np.zeros_like(img)
imgG_colored[:, :, 1] = imgG

imgB_colored = np.zeros_like(img)
imgB_colored[:, :, 2] = imgB

fig, axs = plt.subplots(1, 3)
axs[0].imshow(imgR_colored)
axs[1].imshow(imgG_colored)
axs[2].imshow(imgB_colored)

# fig, axs = plt.subplots(1, 3)
# axs[0].imshow(imgR)
# axs[1].imshow(imgG)
# axs[2].imshow(imgB)

plt.show()
