import cv2
from imutils.paths import list_images
import numpy as np

for names in list_images("poses"): #looks for images in based folder named poses
    img = cv2.imread(names ,cv2.IMREAD_GRAYSCALE)
    ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)

    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)

    cv2.circle(img,center,radius,(127,255,0),3) #draws the circle encompassing the img

    cv2.circle(img,center,3,(127,255,0),3) #draws the center of the circle encompassing the img

    print(center)
    print(radius)

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#https://stackoverflow.com/questions/46002904/weird-center-from-minenclosingcircle-with-opencv-python
#retrieval date #6/4/2020
