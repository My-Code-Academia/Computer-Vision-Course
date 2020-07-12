import cv2
import matplotlib.pyplot as plt

#loading an image

img = cv2.imread('C:/Users/User/Documents/GitHub/Computer-Vision-Course/Images/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg',0)

#displaying an image

cv2.imshow('image',img)

k = cv2.waitKey(0)&0xFF

if k == ord('e'):
    cv2.destroyAllWindows()
elif k == ord('s'):
    #saving an image
    cv2.imwrite('new image.jpg',img)
    cv2.destroyAllWindows()

#Using Matplotlip
plt.imshow(img, cmap = 'gray',interpolation = 'bicubic')
plt.show()




