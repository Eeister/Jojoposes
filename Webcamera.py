import cv2
def camera():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened(): #if webcam can't open
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read() #bool ret indicates whether frame is captured.
                                #frame is the webcam itself 

        cv2.imshow("Input", frame)

        width = 500
        height = 500

        dim = (width,height)

        frame = cv2.resize(frame, dim)

        c = cv2.waitKey(1)#wait for userinput to close it 

        if c == 27: #press esc to close it 
            break

        elif c == 32:
            cv2.imwrite("compare.jpg", frame)
            print("done")
            
            

    cap.release()
    cv2.destroyAllWindows()

def main():
    camera()


if __name__ == "__main__":
    main()

#https://subscription.packtpub.com/book/application_development/9781785283932/3/ch03lvl1sec28/accessing-the-webcam
#accessed 6/5/2020


