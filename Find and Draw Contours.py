import cv2
import numpy as np
from numpy import ndarray

path = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\contt.png'
img=cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,100,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(len(contours))
print(contours[0])
cv2.imshow('origin',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
