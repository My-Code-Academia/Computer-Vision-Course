import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('F:/Python Course/Data Science/gradiant.jpg',0)

#simple thresholding
#binary_thresholding
ret , thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

#binary_inv
ret , thresh2 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)

#truncation
ret, thresh3 = cv2.threshold(img1, 127, 255, cv2.THRESH_TRUNC)

#truncate_to_zero
ret, thresh4 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO)

#truncate_to_zero_inv
ret, thresh5 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO_INV)

images = [img1, thresh1, thresh2, thresh3, thresh4, thresh5]
titles = ['original', 'binary', 'binary_inv', 'trunc', 'to_zero', 'to_zero_inv']


for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
