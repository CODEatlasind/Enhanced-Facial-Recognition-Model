import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
#painting the background
# blank[:]=255,0,0
# blank[200:300,300:400]=255,0,0

# Draw Figures
# Draw rectangle
# cv.rectangle(blank,[0,0,200,300],(255,0,0),2)
# # Draw Filled rectangle
# cv.rectangle(blank,[0,0,200,300],(255,0,0),cv.FILLED)
# #Draw a circle ,thickness>0 unfilled circle, thickness<0 solid circle
# cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),100,(0,0,255),thickness=-1)
# #Draw a line
# cv.line(blank,(100,200),(100,500),(0,255,0),thickness=2)

#put text
# cv.putText(blank,'Hello World',(200,250),cv.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,0,255),thickness=2)
#put text
cv.putText(blank,'Hello World, I am a wanderer looking for salvation',(0,100),cv.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,0,255),thickness=2)
cv.imshow('blue', blank)

cv.waitKey(0)
# img=cv.imread('image/1.jpg ')