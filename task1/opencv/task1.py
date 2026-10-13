import cv2 as cv

img= cv.imread('task1/photos/cat_large.jpg')

cv.imshow(  'Cat', img) 
cv.waitKey(0)

height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]

print('Height:', height)
print('Width:', width)
print('Channels:', channels)

newfilename=input('Enter new filename: ')
cv.imwrite(newfilename+'.jpg', img)

cv.destroyAllWindows()