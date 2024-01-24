import cv2
import numpy as np

path = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject\chela.PNG'
img = cv2.imread(path, 0)

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('T1', 'image', 0, 255, nothing)
cv2.createTrackbar('T2', 'image', 0, 255, nothing)

while True:
    treshold1 = cv2.getTrackbarPos('T1', 'image')
    treshold2 = cv2.getTrackbarPos('T2', 'image')

    canny = cv2.Canny(img, treshold1, treshold2)

    # Display the Canny edge detection result
    cv2.imshow('image', canny)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Break the loop when the 'Esc' key is pressed
        break

cv2.destroyAllWindows()
