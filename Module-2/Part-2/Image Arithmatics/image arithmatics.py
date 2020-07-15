import cv2
import numpy as np

img1 = cv2.imread('F:/Python Course/Data Science/misc/4.1.01.tiff')
img2 = cv2.imread('F:/Python Course/Data Science/misc/4.1.02.tiff')

#addition

img3 = cv2.add(img1,img2)
img4 = img1+img2

#blending

img5 = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image3',img3)
cv2.imshow('image4',img4)
cv2.imshow('image5',img5)

cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
