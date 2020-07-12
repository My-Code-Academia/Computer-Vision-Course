import cv2

img = cv2.imread('F:/Python Course/Data Science/misc/4.1.01.tiff')

#Accessing Image Properties

#shape
#size
#datatype

print(img.shape)
print(img.size)
print(img.dtype)

#Accessing & Modifying Pixel Values

px = img[100,100,2]
print(px)

img[100,100] = [255,255,255]
print(img[100,100])

print(img.item(100,100,2))

img.itemset((100,100,2),10)

print(img.item(100,100,2))

#Image ROI -> Region of Image

eye = img[100:110, 116:136]

img [10:20, 30:50] = eye


#Splitting & Merging Image Channels
b , g, r = cv2.split(img)

img = cv2.merge((b,g,r))

#Making Borders for Images
#cv2.copyMakeBorder(src,top,bottom, left,right, bordertype,value)

BLUE = [255,0,0]
#constant
#reflect fedcba|abcdefgh|hgfedcb
#reflect_101 gfedcb|abcdefgh|gfedcb
#replicate aaaaaaa|abcdefgh|hhhhhhh
#wrap bcdefgh|abcdefgh|abcdefg
img1 = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_WRAP)

cv2.imshow('imag',img1)
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
