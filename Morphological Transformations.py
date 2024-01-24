import cv2
from matplotlib import pyplot as plt
import numpy as np
path = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject\Mona_Lisa.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale mode
_, mask = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
kernel=np.ones((3,3),np.uint8)
print(kernel)
dilatation=cv2.dilate(mask,kernel)
erosion=cv2.erode(mask,kernel)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
title = ['Original Image', 'Binary Mask','dilatation','erosion','opening']
images = [img, mask,dilatation,erosion,opening]

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], cmap='gray')  # Moved cmap='gray' to plt.imshow()
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])  # Hide axis ticks

plt.show()
