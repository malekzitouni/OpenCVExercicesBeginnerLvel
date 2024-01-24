import cv2
import numpy as np
from numpy import ndarray

path = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\chela.PNG'
path1 = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\Mona_Lisa.jpg'

img = cv2.imread(path)
img1 = cv2.imread(path1)
rows, cols, _ = img.shape
img1 = cv2.resize(img1, (cols, rows))
# Assuming both images have the same height, adjust if needed
combined =  np.hstack((img[:, :256], img1[:, :256]))

cv2.imshow('image', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
