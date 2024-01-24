import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\euro.png'
img = cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
b, g, r = cv2.split(img)

# Plot histograms for each channel
plt.hist(gray.ravel(),bins=256,range=[0,256])
#plt.hist(g.ravel(), bins=256, range=[0, 256], color='green')
#plt.hist(b.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
#plt.hist(r.ravel(), bins=256, range=[0, 256], color='red', alpha=0.7)

# Customize the plot
plt.title('Histogram of Pixel Intensities')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
# Display the plot
plt.show()
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
# Display the image
cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()

