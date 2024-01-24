import cv2
import numpy as np
from matplotlib import pyplot as plt

path = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\chela.PNG'
img = cv2.imread(path,0)
lap=cv2.Laplacian(img, cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
img1=cv2.Sobel(img,cv2.CV_64F,1,0)
titles = ['origine','laplacian','sobel']
images = [img,lap,img1]

# Use len(images) instead of a hardcoded value in the range
for i in range(len(images)):
    plt.subplot(1, len(images), i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # Hide axis ticks

plt.show()
