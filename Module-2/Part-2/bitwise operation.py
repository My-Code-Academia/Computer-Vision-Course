import cv2

image1 = cv2.imread('white-black.png',0)
image2 = cv2.imread('white-circle.png',0)

#and

dest_and = cv2.bitwise_and(image1,image2,mask=None)

#or
dest_or= cv2.bitwise_or(image1,image2,mask=None)

#not
dest_not= cv2.bitwise_not(image1,mask=None)

#xor
dest_xor= cv2.bitwise_xor(image1,image2,mask=None)

cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
cv2.imshow('and',dest_xor)
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
