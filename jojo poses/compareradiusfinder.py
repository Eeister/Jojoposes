import cv2
import numpy as np

def radiusfinder():

    img = cv2.imread('foregroundextrpart3blackandwhite.jpg',cv2.IMREAD_GRAYSCALE) #looks at image in grayscale
    ret,thresh = cv2.threshold(img,127,255,0) #converts image to black and white
    contours,hierarchy = cv2.findContours(thresh, 1, 2) #finds contours of image

    cnt = contours[0] #take the first contour
    (x,y),radius = cv2.minEnclosingCircle(cnt) # finds minimum enclosing circle on the contour
    center = (int(x),int(y))
    radius = int(radius)

    return radius


##
##img2 = cv2.imread('foregroundextrblackandwhite.jpg',cv2.IMREAD_COLOR) #reads image in color
##cv2.circle(img2,center,radius,(0,255,0),3) #draws the min enclosing circle
##cv2.circle(img2,center,3,(255,255,0),3) #draws the center of the circle
##cv2.drawContours(img2, [cnt], 0, (0,0,255), 3) #draws all of the contour
##print(center)
##print(radius)
##
##cv2.imshow('image',img2)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
