import cv2 as cv
import numpy as np
def reScaleFrame(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions=(width,height)
    
    return cv.resize(frame, dimensions, cv.INTER_LINEAR)

i1=cv.imread('image/1.jpg')
image=reScaleFrame(i1,0.1)
# cv.imshow("Prac",image)

# #color to greyscale
# gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow("greyscale",gray)

# # bLur image
# blur=cv.GaussianBlur(image,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

# #canny
# # canq=cv.Canny(blur,1,200,)
# # cv.imshow("Canny1",can)
# can=cv.Canny(blur,100,200,5)
# cv.imshow("Canny100",can)

# #dialate
# dial=cv.dilate(can,(3,3),iterations=2)
# cv.imshow("Dialate",dial)

# #erode
# erode=cv.erode(dial,(3,3),iterations=2)
# cv.imshow("Eroded",erode)

# #cropping

# crp=image[0:200,50:500]
# cv.imshow("Crop",crp)

#translateto

# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(image.shape[1],image.shape[0])
#     return cv.warpAffine(image,transMat,dimensions)

# translatedImage=translate(image,-100,-100)
# cv.imshow("Translated",translatedImage)

# #rotate
# def rotateimg(img,angle,rotPoint=None):
#     (height,width)=img.shape[:2]
    
#     if(rotPoint is None):
#         rotPoint=(width//2,height//2)
    
#     rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimension=(width,height)
    
#     return cv.warpAffine(img,rotMat,dimension)

# rotatedimage = rotateimg(image,30);
# cv.imshow("rotated",rotatedimage)

cv.imshow("Original",image)
#flipping
flip=cv.flip(image,1)
cv.imshow("fliped",flip)
    
cv.waitKey(0)