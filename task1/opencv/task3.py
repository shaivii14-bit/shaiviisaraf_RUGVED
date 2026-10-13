import cv2 as cv

img= cv.imread('task1/photos/park.jpg')
cv.imshow(  'Park', img) 

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny=cv.Canny(gray, 125, 175)
cv.imshow('Canny', canny)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

cv.waitKey(0)
cv.destroyAllWindows()
