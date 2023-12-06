from email.mime import image
import sklearn
from skimage import color
from skimage import io
from matplotlib import pyplot as plt

img = io.imread("T-72B3.jpg")

img_grey = color.rgb2gray(img)
plt.imshow(img_grey)
plt.show()