import cv2
import numpy as np
from Webcamera import camera
from scipy.spatial import distance as dist
import pickle
from foregroundextract import *
from compareblackandwhite import compareblackandwhite
from compareradiusfinder import radiusfinder
from comparemoments import zernikemoments
from comparer import compare
from imutils.paths import list_images

camera() #these two functions are out of the main because if they are not then the img variable will read a previous sessions phot
foregroundextrpart1()

windowName = "BackgroundRemover"
img = cv2.imread("foregroundextrpart1.jpg")
(ix,iy) = (-1,-1) #default mouse coord
drawing = False #if mouse isn't pressed then drawing isn't happening


def draw_circle(event, x,y,flags,param):
    global ix, iy,drawing #makes sure to update variables

    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True #we are now drawing. mouse has been clicked
        (ix,iy) = x,y #draws a circle

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x,y), 10,(255,255,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False



def main():
    
    cv2.namedWindow(windowName)
    
    #cv2.setMouseCallback(windowName, draw_circle)

    while(True): #refreshes image everytime
        cv2.imshow(windowName,img)
        cv2.setMouseCallback(windowName, draw_circle)

        if cv2.waitKey(20) == 27:
            break
    cv2.imwrite("foregroundextrpart2.jpg", img)

    cv2.destroyAllWindows()

    foregroundextrpart2()
    compareblackandwhite("foregroundextrpart3.jpg") 
    radius = radiusfinder()
    features = zernikemoments(radius)


    infile = open("moment_dict.p","rb") #opens file filled with jojo image moments
    new_dict = pickle.load(infile)

    finalanswer = compare(new_dict, features)

    finalanswer = finalanswer 

    infile.close()
    comparedimg = cv2.imread("compare.jpg")

    for names in list_images("poses"):
        if finalanswer in names and "and" not in names:
            jojoimg = cv2.imread(names)
            cv2.imshow("jojo", jojoimg)

    cv2.imshow("takenphoto",comparedimg)

    print(finalanswer)
    
    
    
    


if __name__ == "__main__":
    main()
