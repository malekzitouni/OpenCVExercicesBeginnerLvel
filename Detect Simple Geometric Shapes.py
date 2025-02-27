import cv2
import numpy as np
path= r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject.png'
img=cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thrash=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thrash,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx=cv2.approxPolyDP(contour,0.02*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if len(approx)==3:

        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(0,0,0))
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspectratio=float(w)/h
        print(aspectratio)
        if aspectratio>=0.9 and aspectratio<=1:
             cv2.putText(img,"square",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
        else:
            cv2.putText(img,"rectangle",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
    elif len(approx)==6:
        cv2.putText(img,"hexagon",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
    elif len(approx)==5:
          cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
    elif len(approx)==10:
             cv2.putText(img,"star",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
    else:
        cv2.putText(img,"cercle",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))


cv2.imshow("shapes",img)
cv2.waitKey()
cv2.destroyAllWindows()
