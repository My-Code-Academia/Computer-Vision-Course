import cv2

#VideoCapture

cap = cv2.VideoCapture('F:/Python Course/intro.mp4')

#VideoWriter

fourcc = cv2.VideoWriter_fourcc(*'H264') #DIVX MJPG XIVD
out = cv2.VideoWriter('output.mp4', fourcc, 15,(int(cap.get(3)), int(cap.get(4))),True)


while(cap.isOpened()):

    ret ,frame=cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)

        out.write(frame)

        cv2.imshow('frame',frame)

        k = cv2.waitKey(10)&0xFF

        if k == 27:
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
