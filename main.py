from cv2 import cv2
import numpy as np

def effect(dir="vertical", pixelLength=480):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    _ , new_img = cap.read()
    x, y = 0, 0
    w = len(new_img[0])-1 #Cam width
    h = len(new_img)-1 #Cam height
    line_thickness = 2

    if dir=="vertical":
        pixelLength = h
        x_max=w
    else:
        pixelLength = w
        y_max=h
    for i in range(1,pixelLength,1):
        _, img = cap.read()
        
        if dir=="vertical":
            new_img[i,:] = img[i,:]
            img[:i,:] = new_img[:i,:]
            y=i
            y_max=i
        else:
            new_img[:,i] = img[:,i]
            img[:,:i] = new_img[:,:i]
            x=i
            x_max=i
        
        #"Whity" image effect
        sub_img = img[y:y+h, x:x+w]
        white_rect = np.ones(sub_img.shape, dtype=np.uint8) * 255
        res = cv2.addWeighted(sub_img, 0.5, white_rect, 0.5, 1.0)
        img[y:y+h, x:x+w] = res
        #Separation line
        cv2.line(img, (x,y),(x_max,y_max),(0,0,255), line_thickness)

        # Display
        cv2.imshow('img', img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff #ESC
        if k == 27:
            break
    # Release the VideoCapture object
    cap.release()

    #Creates a jpg file
    img_name=input("Put a name to your creation:")
    if (img_name!=""):
        img = img[:-line_thickness-1,:-line_thickness-1]
        cv2.imwrite("images/"+img_name+".jpg",img)
        print("Image created succesfully!")
    else:
        print("No image created!")
#Execution
dir = input("Direction: ")

effect(dir)