import cv2
img1 = cv2.imread('F:/Python Course/Data Science/misc/4.1.01.tiff')
img2 = cv2.imread('logo.png')

rows, cols, channel = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,230, 255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi, mask =mask_inv)

img2_fg= cv2.bitwise_and(img2,img2, mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('res',dst)
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
