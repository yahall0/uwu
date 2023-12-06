import cv2
import numpy as np

img = cv2.imread('lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg', cv2.IMREAD_GRAYSCALE)

min_val = np.min(img)
max_val = np.max(img)
stretched_img = (img - min_val)  / (max_val - min_val)

stretched_img = (stretched_img * 255).astype(np.uint8)


cv2.namedWindow('Contrast Stretched Image', cv2.WINDOW_NORMAL)
    
aspect_ratio = img.shape[1] / img.shape[0]  
    
window_width = 600
window_height = int(window_width / aspect_ratio)

cv2.resizeWindow('Contrast Stretched Image', window_width, window_height)
    
cv2.imshow('Contrast Stretched Image', stretched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()