import cv2
import glob
import matplotlib.pyplot as plt

path = "lab2(upto Minor-1(minus stuff from lab-1))\*.jpg" 
img_files = glob.glob(path)

for file in img_files:
    img = cv2.imread(file)
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img_rgb)
    plt.show()