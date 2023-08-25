import cv2 as cv
cap=cv.VideoCapture(0)
while True:
    isTrue, frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
    can=cv.Canny(blur,50, 100)
    cv.imshow('Video', can)
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
cap.release()
cap.destroyAllWindows()