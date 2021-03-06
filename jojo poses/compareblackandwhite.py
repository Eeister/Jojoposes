import cv2
import numpy as np
import imutils


def compareblackandwhite(name):
    image = cv2.imread(name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converts image to gray scale
    cv2.imshow("deded",image)


    thresh = cv2.bitwise_not(image) #turns image into black and white and flips the pixel color values. black turns to white and white turns to black 
    
    #cv2.imshow("ddd", thresh)
    thresh[thresh < 255] = 0 #converts any pixel not white into black
    #cv2.imshow("dddddd", thresh)
    thresh = cv2.bitwise_not(thresh) #reflips the image so we get an image with a black background and a white foreground
    

    outline = np.zeros(image.shape, dtype = "uint8") #creates new window based on arguments.
                                                     #image.shape gets height, column and color of previous image window.
                                                     #uint8 is used unisigned 8 bit integer, prevents pixel value more than 2^8 -1
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE) #finds external contour of the threshed image. estimates simple 
    cnts = imutils.grab_contours(cnts) #turns the contour a list to make it easier for accessing
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0] #grabs the largest contour based on area of the contour
    cv2.drawContours(outline, [cnts], -1, 255, -1) #draws the contour on the outline, -1 means all contours, 255 is black color, -1 fills inside of outline
 
    #cv2.imshow("r", outline)
    newimagename = name.replace(".jpg","") + "blackandwhite.jpg"
    cv2.imwrite(newimagename,outline) #creates new black and white image
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def main():
    name = input("what is the image: ")
    if ".jpg" not in name:
        main()
    else:
        compareblackandwhite(name)


if __name__ == "__main__":
    main()
