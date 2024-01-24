import cv2
import numpy as np
from matplotlib import pyplot as plt

path = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject\Mona_Lisa.jpg
img = cv2.imread(path)
image1 = cv2.pyrDown(img)
identity_kernel = np.ones((5, 5), np.float32) / 25
Sharpening_Kernel= np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
gaussien_kernel=np.array([[1, 2, 1],[2, 4, 2], [1, 2, 1]])
img1 = cv2.filter2D(img, -1, identity_kernel)
img2 = cv2.filter2D(img, -1, Sharpening_Kernel)
img3 = cv2.filter2D(img, -2, Sharpening_Kernel)
img4=cv2.filter2D(img,-1,gaussien_kernel)
img5=cv2.blur(img,(1,1))
img6=cv2.GaussianBlur(img,(1,1),2)
img7=cv2.medianBlur(img,5)
titles = ['origine','gaussienblur','medianblur']
images = [img,img6,img7]

# Use len(images) instead of a hardcoded value in the range
for i in range(len(images)):
    plt.subplot(1, len(images), i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # Hide axis ticks

plt.show()


