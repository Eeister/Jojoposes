import cv2
from imutils.paths import list_images
import numpy as np
import pickle


radius_dict = dict() #holds min radius info of each image

for names in list_images("poses"): #looks for images in based folder named poses
    if "black" not in names:
        continue
    
    img = cv2.imread(names ,cv2.IMREAD_GRAYSCALE) #converts image to gray
    ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #converts it to binary black and white
    contours,hierarchy = cv2.findContours(thresh, 1, 2) #finds the contour of the image

    cnt = contours[0] #biggest contour
    (x,y),radius = cv2.minEnclosingCircle(cnt) #finds info about the minimum enclosing circle on the contour
    center = (int(x),int(y)) 
    radius = int(radius)

    cv2.circle(img,center,radius,(127,255,0),3) #draws the circle encompassing the img

    cv2.circle(img,center,3,(127,255,0),3) #draws the center of the circle encompassing the img

    radius_dict[names] = radius

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pickle.dump(radius_dict, open("radius_dict.p", "wb")) #dumps info gathered into pickle file


#https://stackoverflow.com/questions/46002904/weird-center-from-minenclosingcircle-with-opencv-python
#retrieval date #6/4/2020
