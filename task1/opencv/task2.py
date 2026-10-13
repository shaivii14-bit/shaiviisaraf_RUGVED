import cv2 as cv

img= cv.imread('task1/photos/cats.jpg') 

scale = float(input('Enter scale factor (0.5 for half size, 2 for double size): '))
width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)
dim = (width, height)
if scale<1:
    resized= cv.resize(img, dim, interpolation=cv.INTER_AREA)
else:
    resized= cv.resize(img, dim, interpolation=cv.INTER_LINEAR)

x1=int(input('Enter x1 coordinate for cropping: '))
y1=int(input('Enter y1 coordinate for cropping: '))
x2=int(input('Enter x2 coordinate for cropping: '))
y2=int(input('Enter y2 coordinate for cropping: '))
cropped= img[y1:y2,x1:x2]

flipped= cv.flip(img,1)

cv.imshow(  'Cats', img)

cv.imshow(  'Resized Cats', resized)
cv.imwrite('/Users/shaiviisaraf/RUGVED/TASK1/photos/ResizedCats.jpg', resized)

cv.imshow('Cropped Cats', cropped)
cv.imwrite('/Users/shaiviisaraf/RUGVED/TASK1/photos/CroppedCats.jpg', cropped)

cv.imshow('Flipped Cats', flipped)
cv.imwrite('/Users/shaiviisaraf/RUGVED/TASK1/photos/FlippedCats.jpg', flipped)

cv.waitKey(0)

cv.destroyAllWindows()

