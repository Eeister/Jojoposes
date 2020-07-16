#resizing all the jojo images

import cv2
from imutils.paths import list_images


for names in list_images("poses"): #looks for images in based folder named poses
    img = cv2.imread(names,cv2.IMREAD_UNCHANGED)

    width = 486
    height = 640
    dim = (width, height)


    resized = cv2.resize(img, dim,cv2.INTER_AREA)

    cv2.imshow("Resized image", resized)
    cv2.imwrite(names,resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    #https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
    # retrieval date 6/1/2020
