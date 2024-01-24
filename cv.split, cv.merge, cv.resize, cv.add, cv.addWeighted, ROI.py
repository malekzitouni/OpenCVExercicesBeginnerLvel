import cv2
import numpy as np

path = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject\Capture.PNG'
path1 = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject\chela.png'
img = cv2.imread(path)
img1 = cv2.imread(path1)
cv2.imshow('firstimage',img)
cv2.imshow('secondimage',img1)
cv2.waitKey(0)
img1 = cv2.resize(img1, (img.shape[1], img.shape[0]))
print(img.shape)
print(img1.shape)
# Adding two images
new_image = cv2.bitwise_or(img, img1)
cv2.imshow('added', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
image2=cv2.addWeighted(img,90,img1,10,0)
cv2.imshow('addded', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# Getting image dimensions
width = img.shape[1]
height = img.shape[0]

# Displaying the original image
cv2.imshow('image', img)
cv2.waitKey(0)

# Printing image size and shape
print("Original Image:")
print("Size:", img.size)
print("Shape:", img.shape)

# Resizing the image
new_width = 500
new_height = 600
img_resized = cv2.resize(img, (new_width, new_height))
cv2.imshow('resized image', img_resized)
cv2.waitKey(0)

# Printing resized image size and shape
print("Resized Image:")
print("Size:", img_resized.size)
print("Shape:", img_resized.shape)

# Splitting and merging channels
b, g, r = cv2.split(img_resized)
img_merged = cv2.merge((b, g, r))

# Displaying the green channel
cv2.imshow('green channel', g)
cv2.waitKey(0)

# Displaying the blue channel (for demonstration purposes)
cv2.imshow('blue channel', b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Printing the blue channel values
print("Blue Channel Values:")
print(b) 
'''
