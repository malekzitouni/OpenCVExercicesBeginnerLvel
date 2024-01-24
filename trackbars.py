import cv2
import numpy as np
from matplotlib   import pyplot as plt
img = np.zeros((300, 512, 3), np.uint8)



def nothing(x):
    print(x)

# Create a window and trackbars
cv2.namedWindow('image')

# Uncomment the following lines if you want to use an image
# cv2.imshow('image', img1)

# Create trackbars for B, G, and R channels
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

while True:
    cv2.imshow('image', img)

    # Get the current trackbar positions
    blue = cv2.getTrackbarPos('B', 'image')
    green = cv2.getTrackbarPos('G', 'image')
    red = cv2.getTrackbarPos('R', 'image')

    # Set the image color based on trackbar positions
    img[:] = [blue, green, red]

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Break the loop when the 'Esc' key is pressed
        break

cv2.destroyAllWindows()
