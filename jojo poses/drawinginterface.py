import numpy as np
import cv2

#create an image window
windowName = "BackgroundRemover"
#img = cv2.imread("foregroundextrpart1.jpg")
#cv2.namedWindow(windowName)
(ix,iy) = (-1,-1) #default mouse coord

drawing = False #if mouse isn't pressed then drawing isn't happening


#mouse callback function
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


#bind callback function to window

def main():
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, draw_circle)



    
    while(True): #refreshes image everytime
        cv2.imshow(windowName,img)
        if cv2.waitKey(20) == 27:
            break

    cv2.imwrite("foregroundextrpart2.jpg", img)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


