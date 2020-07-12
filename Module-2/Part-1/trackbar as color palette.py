import numpy as np
import cv2

def on_change(self):
    pass

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow('trackbar')

#createTrackbar
cv2.createTrackbar('R', 'trackbar', 0, 255, on_change)
cv2.createTrackbar('G', 'trackbar', 0, 255, on_change)
cv2.createTrackbar('B', 'trackbar', 0, 255, on_change)

switch = '0:off 1:on'
cv2.createTrackbar(switch, 'trackbar',0,1, on_change)

while(1):
    cv2.imshow('trackbar', img)

    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R','trackbar')
    g = cv2.getTrackbarPos('G','trackbar')
    b = cv2.getTrackbarPos('B','trackbar')
    s = cv2.getTrackbarPos(switch,'trackbar')

    if s == 0:
        img[:]=0
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()
