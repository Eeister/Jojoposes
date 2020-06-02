#resizing all the jojo images

import os
import cv2

entries = os.listdir("poses")

for names in entries:
    print(names)
    img = cv2.imread(names,  cv2.IMREAD_UNCHANGED)

    
    width = 309
    height = 619
    dim = (width, height)


    resized = cv2.resize(img, dim ,cv2.INTER_AREA)

    cv2.imshow("Resized image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
