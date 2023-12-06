import cv2

img = cv2.imread("lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg")



original_height, original_width = img.shape[:2]

upscale_factor = 2

new_width = int(original_width * upscale_factor)
new_height = int(original_height * upscale_factor)


upsampled_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

aspect_ratio = img.shape[1] / img.shape[0]
window_width = 1080
window_height = int(window_width / aspect_ratio)

cv2.namedWindow('Upsampled Image', cv2.WINDOW_NORMAL)    
cv2.resizeWindow('Upsampled Image', window_width, window_height)
cv2.imshow('Upsampled Image', upsampled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()