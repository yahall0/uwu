import cv2

img = cv2.imread('lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg')

negative_img = 255 - img

cv2.namedWindow('Negative Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Negative Image', 1366, 768)

cv2.imshow('Negative Image', negative_img)

cv2.waitKey(0)
cv2.destroyAllWindows()