import cv2

def camera():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened(): #if webcam can't open
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read() #bool ret indicates whether frame is captured.
                                #frame is the webcam itself 
##
        width = 486
        height = 640
##
        dim = (width,height)
##
        frame = cv2.resize(frame, dim)

        tl = (100,600) #top left coord of rect
        br = (430,100) #bottom right coord of rect

        color = (255,0,0) #color of rect line
        thick = 2 #thickness of rect line

        frame = cv2.rectangle(frame, tl, br, color, thick) #draws rect on image

        cv2.imshow("Input", frame)
        

        c = cv2.waitKey(1)#wait for userinput to close it 

        if c == 27: #press esc to close it 
            break

        elif c == 32:
            width = 486
            height = 640

            dim = (width,height)
            img1 = cv2.resize(frame, dim)
            cv2.imwrite("compare.jpg", img1)
            

            
            print("done")
            
            

    cap.release()
    cv2.destroyAllWindows()

def main():
    camera()


if __name__ == "__main__":
    main()

#https://subscription.packtpub.com/book/application_development/9781785283932/3/ch03lvl1sec28/accessing-the-webcam
#accessed 6/5/2020


