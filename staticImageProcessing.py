import cv2 as cv
import numpy as np

img=cv.imread('image/2.jpg');
cv.imshow('eagle', img);



#contours
#gray
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# cv.imshow("Grey",gray)
blur=cv.GaussianBlur(gray,(3,3),10)
canny=cv.Canny(blur,100,500)
cv.imshow("Contours",canny)
#upper threshold has smaller wjhite pixels and lower threshold has more white
#aperture deefines the sobel filter level

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found')

cv.waitKey(0)