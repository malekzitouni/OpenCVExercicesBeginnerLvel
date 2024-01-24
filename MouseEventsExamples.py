import cv2
import numpy as np
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
def click(event,x,y,flags,par):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strxy=str(x)+','+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,0,0),2)
        cv2.imshow('image',img)
img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click)
cv2.waitKey(0)
cv2.destroyAllWindows()         
