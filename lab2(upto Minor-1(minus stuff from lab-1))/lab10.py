import cv2

img = cv2.imread('lab2(upto Minor-1(minus stuff from lab-1))\lappy.jpg', cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.namedWindow('Binary Image', cv2.WINDOW_NORMAL)
        
cv2.resizeWindow('Binary Image', 1024, 768)

cv2.imshow('Binary Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
