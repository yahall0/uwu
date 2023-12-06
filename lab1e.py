#split a colored image into red blue and green channels and display 
# the original image along with the 3 band separated images

import sklearn
from skimage import color
from skimage import io
from matplotlib import pyplot as plt

img = io.imread("T-90M.jpg")

imgR = img[:, :, 0]
imgG = img[:, :, 1]
imgB = img[:, :, 2]

# plt.imshow(imgR)
# plt.imshow(imgG)
# plt.imshow(imgB)

fig, axs = plt.subplots(1, 3)
axs[0].imshow(imgR)
axs[1].imshow(imgG)
axs[2].imshow(imgB)

plt.show()
