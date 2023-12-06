import cv2

img = cv2.imread('lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg')

original_height, original_width = img.shape[:2]

downscale_factor = 0.5

new_width = int(original_width * downscale_factor)
new_height = int(original_height * downscale_factor)

downsampled_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

cv2.namedWindow('Downsampled Image', cv2.WINDOW_NORMAL)
    
aspect_ratio = img.shape[1] / img.shape[0]  # width / height
    
window_width = 1080
window_height = int(window_width / aspect_ratio)

cv2.resizeWindow('Downsampled Image', window_width, window_height)
    
cv2.imshow('Downsampled Image', downsampled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
