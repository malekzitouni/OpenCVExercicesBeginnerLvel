import cv2
import numpy as np
import matplotlib.pyplot as plt
path1= r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\shapess.png'
path2= r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\templ.png'
img=cv2.imread(path1)
temp=cv2.imread(path2)
res=cv2.matchTemplate(img,temp,cv2.TM_CCORR)
print(res)
cv2.imshow("result",res)
arr=np.array([1,2,3,4,5])
ress=np.where(arr>2)
print(ress)
cv2.waitKey()
cv2.destroyAllWindows()
