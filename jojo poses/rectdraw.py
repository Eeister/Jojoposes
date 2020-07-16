import cv2

image = cv2.imread("compare.jpg")


tl = (100,600)
br = (430,100)


color = (255,0,0)
thick = 2

image = cv2.rectangle(image, tl, br, color, thick) 

cv2.imshow("deedeeeeeeee", image)
c = cv2.waitkey(1)

if c == 27:
    cv2.destroyAllWindows()
