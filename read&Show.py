import cv2 as cv
# showimage

# img=cv.imread('image/1.jpg');
# cv.imshow('eagle', img);
# cv.waitKey(0)

# show video

# cap=cv.VideoCapture('video/1.mp4');
# while True:
#     isTrue, frame=cap.read();
#     cv.imshow('Video', frame)
#     if(cv.waitKey(20) & 0xFF==ord('d')):
#         break
# cap.release()
# cap.destroyAllWindows()

#resize and rescale

def reScaleFrame(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions=(width,height)
    
    return cv.resize(frame, dimensions, cv.INTER_LINEAR)

    
# TYPES of standalone rescaling  for img, video and live videos
# # No resize
# img=cv.imread('image/2.jpg')
# # Resize with self valuesq
# imS = cv.resize(img, (480, 360),cv.INTER_CUBIC)
# # resize with function
# imRes = reScaleFrame(img)

# # Determines the width of the picture
# # print(img.shape[1])
# # cv.imshow('eagle', img)
# # cv.imshow('eagle_resized', imS)
# # cv.imshow('eagle_resized2', imRes)
# cv.waitKey(0)
    
# resizing live video
cap=cv.VideoCapture('video/2.mp4');

# resizing live video
# def changeRes( width, height):
#     cap.set(3,width)
#     cap.set(4, height)
    
    
# while True:
#     isTrue, frame=cap.read();
    
#     reSized=reScaleFrame(frame)
    
#     cv.imshow('Video', frame)
#     cv.imshow('Video_Resized', reSized)
#     if(cv.waitKey(20) & 0xFF==ord('d')):
#         break
# cap.release()
# cap.destroyAllWindows()

cap=cv.VideoCapture(0);

    
while True:
    isTrue, frame=cap.read();
    
    reSized=reScaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', reSized)
    if(cv.waitKey(2) & 0xFF==ord('d')):
        break
cap.release()
cv.destroyAllWindows()


