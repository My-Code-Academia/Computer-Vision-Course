import cv2
import numpy as np

img = cv2.imread('F:/Python Course/Data Science/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg',1)

height,width = img.shape[:2]

#scaling/resizing
res = cv2.resize(img,(2*width,2*height), interpolation = cv2.INTER_LINEAR)

#translation/shifting
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img, M, (width,height))

#rotation
M = cv2.getRotationMatrix2D((width/2,height/2), -90, 2)
dst1 = cv2.warpAffine(img, M, (width,height))

#flipping
dst2 = cv2.flip(img,-1)

#colorspace changing
#gray #hsv [0,179][0,255]

dst3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('image',img)
cv2.imshow('image1',dst3)
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
